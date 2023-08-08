from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# class User(AbstractUser):
#     # name = models.CharField(max_length=50)
#     email = models.CharField(max_length=50, unique=True)
#     username = models.CharField(max_length=50, unique=True)
#     mobile_number = models.CharField(max_length=15, unique=True, blank=True, null=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']

#     def __str__(self):
#         return self.email
    
# class UserProfile(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     profile_pic = models.ImageField(upload_to='profile_pic/')
#     bio = models.TextField(blank=True)
#     date_of_birth = models.DateField()
#     city = models.CharField(max_length=100, blank=True)
#     address = models.CharField(max_length=200, blank=True)

#     def __str__(self):
#         return self.user.username


class CustomUser(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username