from django.shortcuts import HttpResponse

def greeting(request):
    
    html = """<html lang='en'> <body> <h1>test</h1></body></html>"""
    
    return HttpResponse(html)