from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    link_to_about = '<a href="/rango/about/">here</a>'
    response = f'Rango says hey there partner! Here is the about page {link_to_about}.'
    return HttpResponse(response)


def about(request):
    link_to_index = '<a href="/rango/">Index</a>'
    response = f'Rango says here is the about page! Go back to the {link_to_index}.'
    return HttpResponse(response)

