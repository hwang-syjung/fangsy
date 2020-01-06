from django.db import models


# Create your models here.
from django.db.models import CharField


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, blank=False, null=False)
    content = models.TextField(blank=True, null=True)
    schedule = models.DateTimeField()
    location = models.CharField(max_length=100, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
