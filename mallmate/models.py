from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=320)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.email
