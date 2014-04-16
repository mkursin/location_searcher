# coding=utf-8
from django.http import HttpResponse

import httplib
import re
from json import dumps
from xml.dom.minidom import parseString

from searcher.models import LocationsByIp


def get_location_by_ip(request):
    ip = request.GET['ip']

    url = "194.85.91.253:8090"
    conn = httplib.HTTPConnection(url)
    conn.request("POST", "/geo/geo.html",
                 "<ipquery><fields><all/></fields><ip-list><ip>" + ip +
                 "</ip></ip-list></ipquery>")

    resp = conn.getresponse()
    data = resp.read()

    conn.close()

    response = {'status': 'fail', 'ip': ip}
    if not re.search("<message>Not found</message>", data):
        if not LocationsByIp.objects.filter(IP=ip).exists():
            dom = parseString(data)
            city = dom.documentElement.getElementsByTagName('city')[0].firstChild.nodeValue
            region = dom.documentElement.getElementsByTagName('region')[0].firstChild.nodeValue
            district = dom.documentElement.getElementsByTagName('district')[0].firstChild.nodeValue
            lat = dom.documentElement.getElementsByTagName('lat')[0].firstChild.nodeValue
            lng = dom.documentElement.getElementsByTagName('lng')[0].firstChild.nodeValue

            add_db_data = LocationsByIp(IP=ip, City=city, Region=region, Bistrict=district, Longitude=lng, Latitude=lat)
            add_db_data.save()

        response['status'] = 'success'

    return HttpResponse(dumps(response), mimetype='application/json')