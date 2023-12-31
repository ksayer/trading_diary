# Generated by Django 4.2.2 on 2023-06-10 20:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("strategies", "0001_initial"),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Asset",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created"),
                ),
                (
                    "updated",
                    models.DateTimeField(auto_now=True, verbose_name="Updated"),
                ),
                ("symbol", models.CharField(max_length=255, unique=True)),
                (
                    "market",
                    models.CharField(
                        choices=[
                            ("STOCKS", "Stocks"),
                            ("FOREX", "Forex"),
                            ("CRYPTO", "Crypto"),
                        ],
                        max_length=6,
                    ),
                ),
            ],
            options={
                "ordering": ["-updated"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Trade",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created"),
                ),
                (
                    "updated",
                    models.DateTimeField(auto_now=True, verbose_name="Updated"),
                ),
                ("comment", models.TextField(blank=True)),
                ("open_date", models.DateTimeField()),
                ("close_date", models.DateTimeField(blank=True, null=True)),
                ("amount", models.DecimalField(decimal_places=2, max_digits=4)),
                ("result_points", models.IntegerField(blank=True, null=True)),
                (
                    "result_amount",
                    models.DecimalField(blank=True, decimal_places=2, max_digits=9),
                ),
                (
                    "reason_out",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("SL", "Stop Loss"),
                            ("TP", "Take Profit"),
                            ("M", "Manually"),
                        ],
                        max_length=2,
                    ),
                ),
                (
                    "action",
                    models.CharField(
                        choices=[("S", "Sell"), ("B", "Buy")], max_length=1
                    ),
                ),
                (
                    "trend",
                    models.CharField(
                        choices=[("S", "Sell"), ("B", "Buy"), ("U", "Unknown")],
                        max_length=1,
                    ),
                ),
                (
                    "asset",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="trades",
                        to="trades.asset",
                    ),
                ),
                (
                    "trading_tool",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="trades",
                        to="strategies.tradingtool",
                    ),
                ),
            ],
            options={
                "ordering": ["-updated"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="TradeScreenshot",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created"),
                ),
                (
                    "updated",
                    models.DateTimeField(auto_now=True, verbose_name="Updated"),
                ),
                (
                    "timeframe",
                    models.CharField(
                        choices=[
                            ("M1", "M1"),
                            ("M5", "M5"),
                            ("M15", "M15"),
                            ("M30", "M30"),
                            ("H1", "H1"),
                            ("H4", "H4"),
                            ("D1", "D1"),
                        ],
                        max_length=3,
                    ),
                ),
                (
                    "screenshot",
                    filer.fields.image.FilerImageField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.FILER_IMAGE_MODEL,
                    ),
                ),
                (
                    "trade",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="trades.trade",
                    ),
                ),
            ],
            options={
                "ordering": ["-updated"],
                "abstract": False,
            },
        ),
    ]
