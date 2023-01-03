from django.shortcuts import HttpResponse

def greeting(request,n1,n2):
    result = n1 * n2
    
    return HttpResponse(result)