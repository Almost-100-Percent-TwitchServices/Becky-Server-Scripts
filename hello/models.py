from django.db import models
from chatterbot import ChatBot
# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

# class BeckyBot(models.Model):
#     botName = models.CharField(max_length = 50)
#     brain = ChatBot(
#         botName,
#         trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
#     )

#     brain.train('chatterbot.corpus.english')