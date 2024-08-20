from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.conf import settings
import os

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default=os.path.join('img', 'default.jpg'), upload_to='profile_pics')
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img_path = os.path.join(settings.STATICFILES_DIRS[0], 'img', 'default.jpg')
        img = Image.open(img_path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)