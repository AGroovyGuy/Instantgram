from django.db import models
from django.contrib.auth.models import User

class Photo(models.Model):
    path = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now=True)
    description = models.TextField()
    op = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name