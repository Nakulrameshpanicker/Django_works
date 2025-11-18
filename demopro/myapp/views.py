from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# def first(request):
#     return HttpResponse("First page")
# def second(request):
#     return HttpResponse("Second page")

def first(request):
    return render(request,'index.html')
def second(request):
    return render(request,'home.html')