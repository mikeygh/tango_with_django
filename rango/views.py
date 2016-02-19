from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there world!")