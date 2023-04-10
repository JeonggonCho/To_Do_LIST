from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=80)
    category = models.CharField(max_length=10, null=True)
    deadline = models.DateField(null=True)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=False)