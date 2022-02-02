from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    context_dict = {'boldnessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return HttpResponse("Rango says hey there partner!")
    return HttpResponse("Rango says hey there partner! <a href='/rango/about/'>About</a>")
    return render(request, 'rango/index.html', context=context_dict)
def about(request):
    context_dict = {'boldnessage': 'This tutorial has been put together by Yuan Kuang.'}
    return HttpResponse("Rango says here is the about page.")
    return HttpResponse("Rango says hre is the about page. <a href='/rango/'>Index</a>")
    return render(request, 'rango/about.html', context=context_dict)

