from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    deadline = models.DateField(null=True)
    category = models.CharField(max_length=10, null=True)