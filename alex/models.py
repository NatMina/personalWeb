from django.db import models

# Create your models here.


class Education(models.Model):
    institution_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    cert = models.CharField(max_length=50)


class Experience(models.Model):
    employer = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    position = models.CharField(max_length=50)
    location = models.CharField(max_length=50)


class Certification(models.Model):
    certifier = models.CharField(max_length=50)
    date = models.DateField()
    qualification = models.CharField(max_length=50)