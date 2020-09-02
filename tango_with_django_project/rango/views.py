from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    content_text = {'boldmessage': 'This message is depend on you!'}
    return render(request, 'rango/index.html', context=content_text)


def about(request):
    return HttpResponse('Rango says here is about page! <br> <a href="/rango/">Index</a>')
