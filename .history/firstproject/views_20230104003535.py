from django.shortcuts import HttpResponse

def greeting(request,n1,n2):
    result = n1 * n2
    html = "<html lang='en'> <body> <h1>test</h1></body></html>"
    
    return HttpResponse(html)