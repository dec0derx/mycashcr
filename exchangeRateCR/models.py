from django.db import models

# Create your models here.
class BanksInsight(models.Model):
    date = models.DateField(auto_now_add=True)
    insight = models.TextField()

    def __str__(self):
        return f"Insight for {self.date}"