from django.db import models

# Create your models here.

class Course(models.Model):
    name =models.CharField(max_length=200, unique=True,)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="courses/%Y/%m/%d/", default="courses/not_ava.jpg")
    date= models.DateTimeField(auto_now=True)
    available= models.BooleanField(default=True)

    def __str__(self):
        return self.name

