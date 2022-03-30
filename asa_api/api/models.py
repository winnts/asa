from django.db import models

# Create your models here.


class Currency(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField()
    sell = models.DecimalField(max_digits=5, decimal_places=2)
    buy = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
