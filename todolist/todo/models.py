from django.db import models
import datetime

class Todo(models.Model):
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=1000)
    date = models.DateField(("Date"), default=datetime.date.today)

    def __str__(self):
        return self.title