"""
URL configuration for user_authentication project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1.views import Home, Register, UserLogin, UserLogout
from app1.views import Adminhome , Student , Teacher,Otp
urlpatterns = [
path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('adminhome/', Adminhome.as_view(), name='adminhome'),
    path('student/', Student.as_view(), name='student'),
    path('teacher/', Teacher.as_view(), name='teacher'),
    path('register/', Register.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('verify/', Otp.as_view(), name='verify'),
]

