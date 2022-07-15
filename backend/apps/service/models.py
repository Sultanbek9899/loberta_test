from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class URL(models.Model):
    INTERVAL_5 = 5
    INTERVAL_15 = 15
    INTERVAL_30 = 30
    INTERVAL_24 = 24
    INTERVAL_CHOICES = (
        (INTERVAL_5, "Every 5 minutes"),
        (INTERVAL_15, "Every 15 minutes"),
        (INTERVAL_30, "Every 30 minutes",),
        (INTERVAL_24, "Every 24 hours",),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="urls")
    url = models.URLField(unique=True)
    http_status = models.SmallIntegerField( null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    check_interval = models.SmallIntegerField(choices=INTERVAL_CHOICES)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "URL"
        verbose_name_plural = "URLs"
        ordering = ["-created"]

    def __str__(self):
        return f"{self.url} - {self.http_status}"


