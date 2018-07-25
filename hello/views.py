# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.html import escape
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
# 
from .models import Greeting
# 
import nltk
from textblob import TextBlob
# from .beckyUtil import BeckyBot
#

from chatterbot import ChatBot
from rq import Queue
from .worker import conn
# from chatterbot.trainers import ListTrainer
# 
import requests
import json
# # Load Becky
# q = Queue(connection=conn)
# BeckyBot = q.enqueue(BeckyBot("Becky"))

@csrf_exempt
def index(request):
    # test = TextBlob(request.body.decode('utf-8'))
    # body_unicode = request.body.decode('utf-8')
    # body = json.loads(body_unicode)
    # message = body['Message']
    # raise KeyError(request.POST)
    
    # return HttpResponse(escape(repr(request)))

    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        # Load Becky
        # q = Queue(connection=conn)
        # loadBecky = q.enqueue(BeckyBot())
        # decode message from chat
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        message = body['Message']
        # RUN THROUGH CHATBOT BRAIN
        # working test = TextBlob(message)

        if "@becky train:" in message:
            message = message.replace("@becky train:","")
            print( message)
            comment,response = message.split("|")
            print( comment)
            print(response)
            for i in range(15):
                settings.BECKY.train([comment,response])
            response = "MrDestructoid Training Assimilated MrDestructoid"
            print( response)
        else:
            message = message.replace("@becky ","")
            print( message)
            response =  settings.BECKY.get_response(message)
            print(response)
        # textblob return HttpResponse(test.translate(to='es')) 
        return HttpResponse(response)

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

