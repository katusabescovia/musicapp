from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    profile_pic = models.ImageField(upload_to='profile_pic', blank=True)
    bio = models.TextField(blank=True)
    
    def __str__(self):
        return self.username
    
    def get_profile_pic_url(self):
        if self.profile_pic:
            return self.profile_pic.url
        else:
            return '/path/to/default/image.jpg'