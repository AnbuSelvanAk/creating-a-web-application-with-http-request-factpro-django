from django.shortcuts import render
from django.http import HttpResponse
def fact(request):
	a=5
	fact=1
	for i in range(1,a+1):
		fact+=i
	x='<h1><font color="red">VALUE IS...'+str(a)+'FACTORIAL VALUE IS...'+str(fact)+'</font><h1>'
	return HttpResponse(x)
