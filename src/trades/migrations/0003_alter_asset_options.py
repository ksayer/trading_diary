# Generated by Django 4.2.2 on 2023-07-17 20:29

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("trades", "0002_alter_trade_result_amount"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="asset",
            options={"ordering": ["symbol"]},
        ),
    ]