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
        return render(request,'calculater.html',{'message':message,'age':age})
    return render(request,'calculater.html')