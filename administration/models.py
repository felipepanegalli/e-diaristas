from django.db import models


class Service(models.Model):
    ICON_CHOICES = (
        ("twf-cleaning-1", "twf-cleaning-1"),
        ("twf-cleaning-2", "twf-cleaning-2"),
        ("twf-cleaning-3", "twf-cleaning-3"),
    )

    name = models.CharField(max_length=50, null=False, blank=False)
    min_value = models.DecimalField(
        null=False, blank=False, decimal_places=2, max_digits=5
    )
    qtd_hours = models.IntegerField(null=False, blank=False)
    percentage = models.DecimalField(
        null=False, blank=False, decimal_places=2, max_digits=5
    )
    bedroom_hour = models.IntegerField(null=False, blank=False)
    bedroom_hour_price = models.DecimalField(
        null=False, blank=False, decimal_places=2, max_digits=5
    )
    living_room_hour = models.IntegerField(null=False, blank=False)
    living_room_hour_price = models.DecimalField(
        null=False, blank=False, decimal_places=2, max_digits=5
    )
    bathroom_hour = models.IntegerField(null=False, blank=False)
    bathroom_hour_price = models.DecimalField(
        null=False, blank=False, decimal_places=2, max_digits=5
    )
    kitchen_hour = models.IntegerField(null=False, blank=False)
    kitchen_hour_price = models.DecimalField(
        null=False, blank=False, decimal_places=2, max_digits=5
    )
    yard_hour = models.IntegerField(null=False, blank=False)
    yard_hour_price = models.DecimalField(
        null=False, blank=False, decimal_places=2, max_digits=5
    )
    others_hour = models.IntegerField(null=False, blank=False)
    others_hour_price = models.DecimalField(
        null=False, blank=False, decimal_places=2, max_digits=5
    )
    icon = models.CharField(
        null=False, blank=False, choices=ICON_CHOICES, max_length=14
    )
    position = models.IntegerField(null=False)
