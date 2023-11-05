from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('edit-register/', views.EditRegisterView.as_view(), name='edit_register'),
    path("password/", views.ChangePasswordView.as_view(), name='change_password'),
    path('password-success/', views.password_success, name='password_success'),
    path('create-profile/', views.CreateProfileView.as_view(), name='create_profile'),
    path('show-profile/<int:pk>', views.ShowProfileView.as_view(), name='show_profile'),
    path('edit-profile/<int:pk>', views.EditProfileView.as_view(), name='edit_profile'),
]
