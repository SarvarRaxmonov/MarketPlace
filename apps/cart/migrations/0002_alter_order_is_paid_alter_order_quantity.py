# Generated by Django 4.2.1 on 2023-08-20 14:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cart", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="is_paid",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="order",
            name="quantity",
            field=models.PositiveIntegerField(default=1),
        ),
    ]
