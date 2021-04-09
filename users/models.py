from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from PIL import Image


class Profile(models.Model):

    Gjinia = (
        ('Mashkull', 'M'),
        ('Femër', 'F')
        )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gjinia = models.CharField(max_length=8, choices=Gjinia, blank=True, null=True)
    ditlindja = models.DateField(max_length=8, null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', help_text='Ndrysho Fotografinë')


    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 600 or img.width > 600:
            output_size = (600, 600)
            img.thumbnail(output_size)
            img.save(self.image.path)