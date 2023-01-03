from django.shortcuts import HttpResponse

def greeting(request):
    return HttpResponse('Hello, World.')