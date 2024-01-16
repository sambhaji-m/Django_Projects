from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from .models import Calculation

def calculator(request):
    return render(request, 'calculator/calculator.html')

def calculate(request):
    expression = request.GET.get('expression', '')
    try:
        result = eval(expression)
        Calculation.objects.create(expression=expression, result=result)
        response_data = {'result': result}
    except Exception as e:
        response_data = {'error': str(e)}
    return JsonResponse(response_data)





