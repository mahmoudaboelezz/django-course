from django.shortcuts import render,HttpResponse
# import csrf exempt
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def index(request):
    print(request.POST)
    if request.method == 'POST':
        message = request.POST.get('username')
        age = request.POST.get('age')
        return render(request,'users.html',{'message1':message,'age1':age})
    return render(request,'users.html')

def calculate(request):
    if request.method == 'POST':
        number1 = request.POST.get('num1')
        number2 = request.POST.get('num2')
        result = number1 + number2
        return render(request,'calculater.html',{'result':result})
    return render(request,'calculater.html')