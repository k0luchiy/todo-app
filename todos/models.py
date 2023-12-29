from django.db import models
from django.conf import settings

# Create your models here.

class Todo(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, 
                             on_delete=models.CASCADE)
    action = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title