from django.db import models

class Mobiles(models.Model):
    mob_id=models.CharField(max_length=50,primary_key=True)
    mob_name=models.CharField(max_length=120)
    brand=models.CharField(max_length=120)
    price=models.PositiveIntegerField(max_length=120)
    color=models.CharField(max_length=120)
    memory=models.PositiveIntegerField(max_length=50)
# Create your models here.
