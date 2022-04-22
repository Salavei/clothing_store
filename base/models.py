from django.db import models


class Items(models.Model):
    first_photo = models.ImageField(verbose_name='первое фото', null=True)
    second_photo = models.ImageField(verbose_name='второе фото', null=True)
    name = models.CharField(max_length=50, verbose_name='название одежды')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='стоимость')
    link_kufar = models.URLField(verbose_name='ссылка на куфар')

    def __str__(self):
        return self.name
