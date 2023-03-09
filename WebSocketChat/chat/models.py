from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Message(models.Model):
    message = models.TextField()
    username = models.CharField(max_length=10)
    pub_date = models.DateTimeField(auto_now_add=True)

