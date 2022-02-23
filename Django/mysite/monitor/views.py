from django.shortcuts import render
from django.http import HttpResponse

def index(request):
#    return HttpResponse("Hello Lee! '" + msg + "'")
    params = {
             'title': 'Django',
             'msg': 'Django test',
             'goto': 'next',
    }
    return render(request, 'initial_page/index.html', params)

def next(request):
    params = {
             'title': 'Django Next Page',
             'msg': 'Next Page!',
             'goto': 'index',
    }
    return render(request, 'initial_page/index.html', params)
