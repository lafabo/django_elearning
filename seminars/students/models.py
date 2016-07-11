from django.db import models
from django.conf import settings


# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)


class Company(models.Model):
    company = models.OneToOneField(settings.AUTH_USER_MODEL)
    company_name = models.CharField(max_length=200)
    company_site = models.URLField(max_length=200)
    company_info = models.TextField(blank=True)
    company_stuff = models.ManyToManyField(Student, verbose_name='Company staff')
