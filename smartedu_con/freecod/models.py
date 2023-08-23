from django.db import models

class Freecode(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=False)
    m1= models.TextField(max_length=111, blank=True)
    m2= models.TextField(max_length=111, blank=True)
    m3= models.TextField(max_length=111, blank=True)
    m4= models.TextField(max_length=111, blank=True)
    m5= models.TextField(max_length=111, blank=True)
    m6= models.TextField(max_length=111, blank=True)
    m7= models.TextField(max_length=111, blank=True)
    m8= models.TextField(max_length=111, blank=True)
    m9= models.TextField(max_length=111, blank=True)
    m10= models.TextField(max_length=111, blank=True)
    m11= models.TextField(max_length=111, blank=True)
    