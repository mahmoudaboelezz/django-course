from django.shortcuts import HttpResponse,render

def greeting(request):
    # result = n1 * n2
    html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<h1>tewer</h1>
<h2>tewer</h2>
    
</body>
</html>'''
    
    return HttpResponse(html)

#render html page from templates
def renderpage(request):
    return render(request,'index.html')