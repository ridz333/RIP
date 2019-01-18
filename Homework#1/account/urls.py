from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('reg/', views.AccountRegistrationView.as_view(), name='reg'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('about/<str:username>/', views.AboutProfileView.as_view(), name='about'),
    path('edit/', views.EditProfileView.as_view(), name='edit')
]