from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class PostModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.FileField(upload_to='uploads/')
    desc = models.TextField(null=True)

    def __str__(self):
        return f'{self.user.username} >> {self.title}'

