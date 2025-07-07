from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status, permissions, filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .permissions import CustomUserPermission
from .serializers import RegisterSerializer, LoginSerializer, ChangePasswordSerializer, UserSerializer, GroupSerializer

User = get_user_model()


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_me_view(request):
    user = request.user
    return Response({
        "id": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "phone": user.phone,
        "is_staff": user.is_staff,
        # هر فیلد دلخواه دیگه هم می‌تونی بدی
    })


class RegisterUserAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = serializer.validated_data['phone']
        password = serializer.validated_data['password']
        user = authenticate(request, phone=phone, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutAPIView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordAPIView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, queryset=None):
        return self.request.user

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Check old password
        if not self.object.check_password(serializer.validated_data['old_password']):
            return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)

        # Set new password
        self.object.set_password(serializer.validated_data['new_password'])
        self.object.save()
        return Response({"data": "Password updated successfully"}, status=status.HTTP_200_OK)


class UserProfileAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 10  # تعداد آیتم‌ها در هر صفحه


class UserListAPIView(generics.ListCreateAPIView):
    """
    لیست کاربران با امکان جستجو و فیلتر
    """
    serializer_class = UserSerializer
    permission_classes = [CustomUserPermission]
    queryset = User.objects.all().order_by('-date_joined')
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        if serializer.validated_data.get('is_superuser') and not self.request.user.is_superuser:
            raise PermissionDenied('شما اجازه ساخت کاربر سوپریوزر را ندارید.')
        serializer.save()

    search_fields = [
        'phone',
        'first_name',
        'last_name',
    ]
    filterset_fields = [
        'is_active',
        'is_staff',
        'is_superuser',
    ]


class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [CustomUserPermission]
    queryset = User.objects.all()


class GroupListView(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [CustomUserPermission]
