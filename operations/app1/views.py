from django.shortcuts import render

# Create your views here.
def addition(request):
    if (request.method=='GET'):
     return render(request,'addition.html')
    if (request.method=='POST'):
        print(request.POST)
        n1=request.POST['num1']
        n2=request.POST['num2']
        s=int(n1)+int(n2)
        print(s)
        context={'result':s,'num1':n1,'num2':n2}

        return render(request, 'addition.html',context)
