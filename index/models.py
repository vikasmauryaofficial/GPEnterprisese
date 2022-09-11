from ast import Return
from django.db import models

# Create your models here.
class Category(models.Model):
    name_ct=models.CharField(max_length=120)
    desc_ct=models.CharField(max_length=120)
    imgct=models.ImageField(upload_to="categ")
    updated_on=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name_ct

class service(models.Model):
    categ=models.ForeignKey(Category,on_delete=models.CASCADE, default=1)
    name=models.CharField(max_length=120)
    desc=models.TextField()
    srimg=models.ImageField(upload_to="pics")
    price=models.PositiveIntegerField()
    updated_on=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


