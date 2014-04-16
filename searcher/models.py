#-*- coding: utf-8 -*-
from django.db import models


class LocationsByIp(models.Model):

    ID = models.IntegerField(verbose_name='ID', db_index=True)
    IP = models.CharField(unique=True, verbose_name='IP',name='IP', max_length=20, db_index=True)
    Latitude = models.FloatField(verbose_name='Долгота', db_index=True)
    Longitude = models.FloatField(verbose_name='Широта', db_index=True)
    City = models.CharField(max_length=50, verbose_name='Город', db_index=True)
    Region = models.CharField(max_length=50, verbose_name='Область', db_index=True)
    Bistrict = models.CharField(max_length=50, verbose_name='Округ', db_index=True)
    Datetime = models.DateTimeField(verbose_name='Дата', db_index=True, auto_now_add=True)

    class Meta:
        db_tablespace = 'locations'
        db_table = 'geoip_table'
        # verbose_name_plural = 'Координаты пользователя'
        # verbose_name = 'Местоположение пользователя'



