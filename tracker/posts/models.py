from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=75)
    category = models.CharField(max_length=100, null=True, blank=True)
    author = models.CharField(max_length=255, null=True, blank=True)
    distribution_expense = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    #date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title