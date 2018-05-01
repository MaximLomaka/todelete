from django.db import models


# Create your models here.
class Education(models.Model):
    name = models.CharField(max_length=30)
    start_date = models.DateTimeField()
    finish_date = models.DateTimeField()


class Phone(models.Model):
    phone = models.CharField(max_length=15)
    phone2 = models.CharField(max_length=15)


class Person(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField()
    image = models.ImageField()
    b_date = models.DateTimeField()
    address = models.CharField(max_length=15)
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    education = models.ForeignKey(Education, on_delete=models.CASCADE)
