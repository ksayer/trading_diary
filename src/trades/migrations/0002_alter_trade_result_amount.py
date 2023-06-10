# Generated by Django 4.2.2 on 2023-06-10 20:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("trades", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="trade",
            name="result_amount",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=9, null=True
            ),
        ),
    ]