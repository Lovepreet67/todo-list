from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import ForeignKey

class task(models.Model):
    task_disc = models.CharField(max_length=300)
    def __str__(self):
        return self.task_disc

class user_field(models.Model):
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    date_of_birth = models.DateField()
    def __str__(self):
        return self.username   


class relation(models.Model):
    user_r = models.ForeignKey(user_field ,on_delete=models.CASCADE )
    task_r = models.ForeignKey(task  ,on_delete=models.CASCADE )
    time = models.TimeField()
    def __str__(self):
        return  self.task_r.task_disc