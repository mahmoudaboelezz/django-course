from django.shortcuts import HttpResponse

def greeting(request):
    # result = n1 * n2
    html = '<html lang="en"><body><h1>tewer</h1></body></html>'
    
    return HttpResponse(html)