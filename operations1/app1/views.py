from math import factorial
from django.shortcuts import render
from django.views import View
from .forms import AdditionForm
from .forms import SignupForms# ✅ import your form properly

class Addition(View):
    def get(self, request):
        form_instance = AdditionForm()
        context = {'form': form_instance}
        return render(request, 'addition.html', context)

    def post(self, request):
        form_instance = AdditionForm(request.POST)

        if form_instance.is_valid():
            n1 = form_instance.cleaned_data['num1']
            n2 = form_instance.cleaned_data['num2']
            result = n1 + n2

        context = {
            'form': form_instance,
            'result': result
        }
        return render(request, 'addition.html', context)

from django.shortcuts import render
import math

class Bf(View):
    def get(self, request):
        context = {
            'num': '',
            'result': '',
            'height': '',
            'weight': '',
            'bmi_result': '',
            'operation': ''
        }
        return render(request, 'Bf.html', context)

    def post(self, request):
        context = {
            'num': '',
            'result': '',
            'height': '',
            'weight': '',
            'bmi_result': '',
            'operation': ''
        }

        if 'factorial_submit' in request.POST:
            n = request.POST.get('num')
            if n:
                n = int(n)
                result = math.factorial(n)
                context['num'] = n
                context['result'] = result
                context['operation'] = 'factorial'

        elif 'bmi_submit' in request.POST:
            weight = request.POST.get('weight')
            height = request.POST.get('height')
            if weight and height:
                weight = float(weight)
                height = float(height)
                bmi = weight / (height * height)
                context['weight'] = weight
                context['height'] = height
                context['bmi_result'] = bmi
                context['operation'] = 'bmi'
        return render(request, 'Bf.html', context)


from django.shortcuts import render
import math
class Signup(View):
    def get(self, request):
        form_instance = SignupForms()
        context = {'form': form_instance}
        return render(request, 'signup.html', context)

    def post(self, request):
        form_instance = SignupForms(request.POST)

        if form_instance.is_valid():
            name = form_instance.cleaned_data['name']
            psw = form_instance.cleaned_data['psw']
            email = form_instance.cleaned_data['email']
            phone = form_instance.cleaned_data['phone']
            add = form_instance.cleaned_data['add']


        context = {
            'form': form_instance,
            'details': {
                'name': name,
                'email': email,
                'phone': phone,
                'address': add
            }
        }
        return render(request, 'signup.html', context)