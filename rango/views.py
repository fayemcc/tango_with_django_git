from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there Partner! \n\n For more information, please visit http://127.0.0.1:8000/rango/about/")

def about(request):
    return HttpResponse("Rango says here is the about page!")