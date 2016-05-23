from django.db import models
from django.contrib.auth.models import User
class Question(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User)

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, null=True)
    author = models.ForeignKey(User)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.text
# Create your models here.
