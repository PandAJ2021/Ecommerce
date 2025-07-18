from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='user_registration'),
    path('logout/', views.UserLogoutView.as_view(), name='user_logout'),
]