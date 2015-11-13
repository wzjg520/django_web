from django.http import HttpResponse
import datetime

def current_time(request):
    now = datetime.datetime.now()
    html = '<html><body>it is %s.</body></html>' % now
    return HttpResponse(html)

def hello(request):
	html = '<h1>hello</h1>'
	return HttpResponse(html)