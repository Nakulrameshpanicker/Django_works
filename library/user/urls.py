from django.urls import path
from . import views
from user.views import  Register

from .views import UserLogin,UserLogout

app_name = "user"

urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
]
