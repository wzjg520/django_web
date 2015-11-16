import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    content = models.CharField(max_length=200)
    addtime = models.DateTimeField('addtime')

    def was_published_recently(self):
        return self.addtime >= timezone.now() - datetime.timedelta(days=1)

    # was_published_recently.admin_order_field = addtime
    # was_published_recently.boolean = True
    # was_published_recently.short_description = 'published rencently ?'

    def __str__(self):
        return self.content


class Choice(models.Model):
    question_id = models.IntegerField()
    content = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.content
