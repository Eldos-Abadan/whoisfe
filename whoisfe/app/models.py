from django.db import models

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.image.name


# Create your models here.
