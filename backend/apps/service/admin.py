from django.contrib import admin

# Register your models here.

from backend.apps.service.models import URL


@admin.register(URL)
class URLAdmin(admin.ModelAdmin):
    list_display = [
        'url',
        'http_status',
        'created',
        'updated',
        'check_interval',
    ]
    list_filter = [
        'created',
        'http_status',
    ]


