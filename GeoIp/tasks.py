#-*- coding: utf-8 -*-
from celery import Celery


app = Celery('tasks', broker='redis://localhost')


@app.task
def getGeoData(ip):

    """Получить город по ip-адресу (адрес предается как строка).
    Возвращает словарь с элементами-строками city, region, district, lat, lng
    """

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