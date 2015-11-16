from django.shortcuts import render
from django.http import HttpResponse


def index(index):
    return HttpResponse('hello word')

def detail(request, question_id):
    return HttpResponse('you are looking at question %s' % question_id)

def results(request, question_id):
    response = 'you are looking at the results %s.'
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse('you are voting at question %s.' % question_id)
