from django.db import models
from django.utils import timezone

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=320)
    password = models.CharField(max_length=128)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.email

class UserPasswordResetRequest(models.Model):
   request_id = models.CharField(max_length=16, unique=True)
   user_email = models.EmailField()
   create_datetime = models.DateTimeField(auto_now_add=True)
   duration = models.PositiveSmallIntegerField(default=10)
   valid = models.BooleanField(default=True)

   class Meta:
       db_table = 'UserPasswordResetRequest'

   def is_expired(self):
       now = timezone.now()
       return (now - self.create_datetime).seconds > (self.duration * 60) or self.valid == False
   def get(self):
       return user_email

   def get_user_email(self):
       return self.user_email

