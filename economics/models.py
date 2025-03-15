from django.db import models

# Create your models here.
class ExchangeRateSummary(models.Model):
    date = models.DateField(auto_now_add=True)
    summary = models.TextField()

    def __str__(self):
        return f"Summary for {self.date}"