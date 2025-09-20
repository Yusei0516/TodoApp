from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todos", )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def is_overdue(self):
        return bool(self.due_date) and not self.is_done and self.due_date < timezone.localdate()
    

    class Meta:
        ordering = ["is_done", "-created_at"]

    def __str__(self):
        return self.title

# Create your models here.
