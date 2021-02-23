import datetime

from django.db import models
from django.utils import timezone
from django.utils.timezone import now

# Create your models here.

class Task(models.Model):
    label =  models.CharField(max_length=30)
    pub_date = models.DateTimeField('Date Created',default=now, editable=False)    
    quantity = models.SmallIntegerField()
    archive = models.BooleanField(default=False)
    notes = models.TextField(editable=True)


    def __str__(self):
        return self.label

    def date_created(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)