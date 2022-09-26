from django.db import models
from django.contrib.auth import get_user_model
user = get_user_model()

class Task(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    title = models.TextField()
    description = models.TextField()
