from django.db import models

class UserModel(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)

    dob = models.DateField()
    grade = models.SmallIntegerField()