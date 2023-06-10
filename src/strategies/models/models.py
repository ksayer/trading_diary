from django.db import models

from admintools.models import CoreModel


class TradingTool(CoreModel):
    title = models.CharField(max_length=255)
    description = models.CharField()

    def __str__(self):
        return self.title
