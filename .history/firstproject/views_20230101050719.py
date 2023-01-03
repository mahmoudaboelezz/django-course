from django.shortcuts import HttpResponse

def greeting():
    return HttpResponse('Hello, World.')