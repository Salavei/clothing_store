from django.db import models


class Items(models.Model):
    photo = models.ImageField()
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    link_kufar = models.URLField()

    def __str__(self):
        return self.name
