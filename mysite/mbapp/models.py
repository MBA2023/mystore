from django.db import models

class devices(models.Model):
    name = models.CharField(max_length=100)
    count = models.IntegerField()
    cost = models.IntegerField()
    weight = models.IntegerField()
    date_of_appear = models.DateField(auto_now=True)
    power = models.IntegerField()
    capacity = models.FloatField()
    category_id = models.IntegerField()

class Category(models.Model):
    category_id = models.IntegerField()
    name = models.CharField(max_length = 200)