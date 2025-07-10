from django.urls import path

from .views_api import (
    RegisterUserAPIView, LoginAPIView, LogoutAPIView,
    ChangePasswordAPIView, UserProfileAPIView,
    UserListAPIView, UserDetailAPIView, user_me_view, GroupListView, GroupDetailAPIView, group_permissions,
    get_all_permissions
)

urlpatterns = [
    path('register/', RegisterUserAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('change-password/', ChangePasswordAPIView.as_view(), name='change-password'),
    path('profile/', UserProfileAPIView.as_view(), name='profile'),
    path('users/', UserListAPIView.as_view(), name='user-list'),
    path('user/me', user_me_view, name='user_me_view'),
    path('users/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
    path('groups/', GroupListView.as_view(), name='group-list'),
    path('groups/<int:pk>/', GroupDetailAPIView.as_view(), name='group-detail'),
    path('groups/<int:group_id>/permissions/', group_permissions),
    path('permissions/', get_all_permissions),

]
