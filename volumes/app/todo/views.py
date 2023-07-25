from django.http import HttpResponse

def say(request):
	return HttpResponse("<h1>hello amin</h1>")