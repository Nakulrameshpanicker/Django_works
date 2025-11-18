from django.shortcuts import render
import math

def cal(request):
    context = {
        'num': '',
        'result': '',
        'height': '',
        'weight': '',
        'bmi_result': '',
        'operation': ''
    }

    if request.method == 'POST':
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
                bmi =(weight / (height * height))
                context['weight'] = weight
                context['height'] = height
                context['bmi_result'] = bmi
                context['operation'] = 'bmi'

    return render(request, 'cal.html', context)
