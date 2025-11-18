from django.shortcuts import render
from django.views import View
from user.forms import RegisterForm , LoginForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.
class Register(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()  # automatically hashes password
            messages.success(request, "Registration successful! Please log in.")
            return redirect('user:login')  # include namespace
        return render(request, 'register.html', {'form': form})



class UserLogin(View):
    def post(self,request):
        form_instance=LoginForm(request.POST)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            u=data['username']
            p=data['password']
            user=authenticate(username=u,password=p)
            if user:
                login(request,user)
                return redirect('book:viewbooks')
            else:
                #print("invalid user")
                messages.error(request, "error logging in, kindly signup")
                return redirect('user:login')
    def get(self, request):
        form_instance=LoginForm()
        context={'form':form_instance}
        return render(request, 'login.html',context)


class UserLogout(View):
    def get(self, request):
        logout(request)
        return redirect('book:home')
