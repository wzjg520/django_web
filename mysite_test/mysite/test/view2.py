from django.http import HttpResponse
def hello(request):
    html = 'hello'
    return HttpResponse(html)