from django.shortcuts import render,HttpResponse
# import csrf exempt
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def index(request):
    
    return render(request,'calculater.html')