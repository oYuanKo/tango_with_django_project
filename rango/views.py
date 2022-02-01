from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("Rango says hey there partner!")
    return HttpResponse("Rango says hey there partner! <a href='/rango/about/'>About</a>")
    context_dict = {'boldnessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context_dict)
def about(request):
    return HttpResponse("Rango says here is the about page.")
    return HttpResponse("Rango says hre is the about page. <a href='/rango/'>Index</a>")
# Create your views here.
