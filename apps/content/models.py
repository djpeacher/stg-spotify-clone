from django.db import models


class City(models.Model):
    name = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Cities"
