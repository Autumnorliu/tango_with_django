from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    content_text = {'boldmessage': 'This message is depend on you!'}
    return render(request, 'rango/index.html', context=content_text)


def about(request):
    return render(request, 'rango/about.html')
