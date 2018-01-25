from django.db import models
from django.contrib.auth.models import User


class Photo(models.Model):
    photo = models.ImageField(upload_to='home/konrad/Pulpit/Instantgram/Instantgram/foteczki/images', null=True, blank=True)
    creation_date = models.DateTimeField(auto_now=True)
    description = models.TextField()
    op = models.ForeignKey(User, on_delete=models.CASCADE)

class Likes(models.Model):
    photo_id = models.ForeignKey(Photo, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name