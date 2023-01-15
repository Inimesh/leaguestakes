from django.http import HttpResponse

def index(request):
    return HttpResponse(b'Hello, you have hit the index view!')
