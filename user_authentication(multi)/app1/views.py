from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views import View
from app1.forms import RegisterForm
from django.contrib import messages

from app1.forms import LoginForm


class Home(View):
    def get(self, request):
        return render(request, 'home.html')

class Adminhome(View):
    def get(self, request):
        return render(request, 'admin.html')

class Student(View):
    def get(self, request):
        return render(request, 'student.html')


class Teacher(View):
    def get(self, request):
        return render(request, 'teacher.html')




class Register(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            messages.success(request, "Registration successful! Please log in.")
            return redirect('login')
        return render(request, 'register.html', {'form': form})


class UserLogin(View):
    def post(self,request):
        form_instance=LoginForm(request.POST)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            u=data['username']
            p=data['password']
            user=authenticate(username=u,password=p)
            if user and user.is_superuser==True:
                login(request,user)
                return redirect('adminhome')
            elif user and user.role=='student':
                login(request, user)
                return redirect('student')

            elif user and user.role == 'teacher':
                login(request, user)
                return redirect('teacher')

            else:
                #print("invalid user")
                messages.error(request, "error logging in, kindly signup")
                return redirect('login')
    def get(self, request):
        form_instance=LoginForm()
        context={'form':form_instance}
        return render(request, 'login.html',context)


class UserLogout(View):
    def get(self, request):
        logout(request)
        return redirect('login')
