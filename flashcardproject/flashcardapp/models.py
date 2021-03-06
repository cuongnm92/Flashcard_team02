from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class wrapUser(models.Model):
    user = models.ForeignKey(User)

class FlashCard(models.Model):
    title = models.CharField(max_length = 255, null = True)
    description = models.CharField(max_length = 500 , null = True)
    grade = models.CharField(max_length = 255 , null = True)
    subject = models.CharField(max_length = 255 , null = True)
    user = models.ForeignKey(User, unique=False)
    vote  =  models.IntegerField()
    uservote = models.ManyToManyField(wrapUser,blank=True,null=True)

    def copy(self, flashcard):
        self.title = flashcard.title
        self.description = flashcard.description
        self.grade = flashcard.grade
        self.subject = flashcard.subject

    def __unicode__(self):
        return u'%s %s %s %s' % (self.title,self.description,self.grade,self.subject)

class Question(models.Model):
    prompt = models.CharField(max_length = 500)
    answer = models.CharField(max_length = 500)
    flashcardID = models.ForeignKey(FlashCard)

    def __unicode__(self):
        return u'%s %s' % (self.prompt,self.answer)
