#-*- coding: utf-8 -*-
from django.db import models


class IP(models.Model):
    def getGeoData(ip):

        import httplib
        import re
        from xml.dom.minidom import parseString

        url = "194.85.91.253:8090"
        conn = httplib.HTTPConnection(url)
        conn.request("POST", "/geo/geo.html",
                     "<ipquery><fields><all/></fields><ip-list><ip>" + ip +
                     "</ip></ip-list></ipquery>")
        resp = conn.getresponse()

        data = resp.read()

        conn.close()

        # если ничего не найдено
        if re.search("<message>Not found</message>", data):
            return None

        dom = parseString(data)
        city = dom.documentElement.getElementsByTagName('city')[0] \
            .firstChild.nodeValue
        region = dom.documentElement.getElementsByTagName('region')[0] \
            .firstChild.nodeValue
        district = dom.documentElement.getElementsByTagName('district')[0] \
            .firstChild.nodeValue
        lat = dom.documentElement.getElementsByTagName('lat')[0] \
            .firstChild.nodeValue
        lng = dom.documentElement.getElementsByTagName('lng')[0] \
            .firstChild.nodeValue

        return {'city': city, 'region': region, 'district': district, 'lat': lat, 'lng': lng}
    a = getGeoData('91.215.190.136')
    for key in sorted(a.iterkeys()):
        print "%s: %s" % (key, a[key])


class LocationsIp(models.Model):
    """
    запись даленных данных в базу
   """
    ID = models.IntegerField(verbose_name='ID')
    IP = models.IntegerField(verbose_name='IP')
    Latitude = models.FloatField(verbose_name='Долгота')
    Longitude = models.FloatField(verbose_name='Широта')
    city = models.CharField(max_length=50, verbose_name='Город') =
    Region = models.CharField(max_length=50, verbose_name='Область')
    Bistrict = models.CharField(max_length=50, verbose_name='Округ')
    Datetime = models.DateTimeField(verbose_name='Дата')

    def save(self, *args, **kwargs):
        super(LocationsIp, self).save(*args, **kwargs)

    class Meta:
        db_table = 'geoip_locations'
        verbose_name_plural = 'Координаты пользователя'
        verbose_name = 'Местоположение пользователя'
