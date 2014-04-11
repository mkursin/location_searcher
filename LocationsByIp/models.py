#-*- coding: utf-8 -*-
from django.db import models


class LocationIp(models.Model):

    ID = models.IntegerField(verbose_name='ID')
    IP = models.IntegerField(verbose_name='IP')
    Latitude = models.FloatField(verbose_name='Долгота')
    Longitude = models.FloatField(verbose_name='Широта')
    City = models.CharField(max_length=50, verbose_name='Город')
    Region = models.CharField(max_length=50, verbose_name='Область')
    Bistrict = models.CharField(max_length=50, verbose_name='Округ')
    Datetime = models.DateTimeField(verbose_name='Дата')

    class Meta:
        db_table = 'geoip_table'
        # verbose_name_plural = 'Координаты пользователя'
        # verbose_name = 'Местоположение пользователя'

p = LocationIp(City='Moscow', Region='Брянская область')
p.save()





