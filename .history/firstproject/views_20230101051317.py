from django.shortcuts import HttpResponse

def greeting(request,name):
    return HttpResponse(f'Hello, {name}')