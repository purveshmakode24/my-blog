from django.http import HttpResponse 
from django.shortcuts import  render
import datetime

def hello(request):
	return render ( request ,  'Accounts/login.html')


def time(request):
	now =  datetime.datetime.now() 
	html  =  "<html><body>  It is now %s</html></body>"%now
	return HttpResponse(now)

def addtime(request ,  offset):
	t  =   int(offset)
	dt  =  datetime.datetime.now() + datetime.timedelta(hours = t)
	html  = "<html><body> After %s it would be %s </html></body>"% (t ,  dt)
	return HttpResponse(html)