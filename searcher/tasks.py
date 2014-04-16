from __future__ import absolute_import

from celery import shared_task


@shared_task
def get_location_by_ip(ip):
    return ip