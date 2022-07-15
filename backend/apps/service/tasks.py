from huey.contrib.djhuey import task, db_task, periodic_task
from huey import crontab

import requests

from .models import URL


@db_task()
def get_update_all_urls(user):
    urls = URL.objects.filter(user=user, is_active=True)
    for url in urls:
        res = requests.get(url.url)
        url.http_status = res.status_code
        url.save(update_fields=["http_status"])


@task()
def get_url_status_code(instance):
    response = requests.get(instance.url)
    instance.http_status = response.status_code
    instance.save(update_fields=["http_status"])


@periodic_task(crontab(minute="*/15"))
def update_every_fifteen_min():
    urls = URL.objects.filter(check_interval=URL.INTERVAL_15, is_active=True)
    for url in urls:
        res = requests.get(url.url)
        url.http_status = res.status_code
        url.save(update_fields=["http_status"])


@periodic_task(crontab(minute="*/5"))
def update_every_five_min():
    urls = URL.objects.filter(check_interval=URL.INTERVAL_5, is_active=True)
    for url in urls:
        res = requests.get(url.url)
        url.http_status = res.status_code
        url.save(update_fields=["http_status"])


@periodic_task(crontab(minute="*/30"))
def update_every_thirty_min():
    urls = URL.objects.filter(check_interval=URL.INTERVAL_30, is_active=True)
    for url in urls:
        res = requests.get(url.url)
        url.http_status = res.status_code
        url.save(update_fields=["http_status"])


@periodic_task(crontab(minute=0, hour="*/24")) # EVERY 24 hours
def update_every_twentyfour_hours():
    urls = URL.objects.filter(check_interval=URL.INTERVAL_24, is_active=True)
    for url in urls:
        res = requests.get(url.url)
        url.http_status = res.status_code
        url.save(update_fields=["http_status"])
