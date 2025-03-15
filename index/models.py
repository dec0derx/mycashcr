from django.db import models

# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=50)
    comment = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.name} ({self.comment})"