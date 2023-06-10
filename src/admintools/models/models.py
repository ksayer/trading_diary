from django.db import models


class CoreModel(models.Model):
    """
    Abstract main model
    """

    created = models.DateTimeField(
        'Created',
        null=False,
        auto_now_add=True,
        editable=False,
    )

    updated = models.DateTimeField(
        'Updated',
        null=False,
        auto_now=True,
        editable=False,
    )

    class Meta:
        abstract = True
        ordering = ['-updated']
