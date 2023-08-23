# Generated by Django 4.2.1 on 2023-08-23 14:33

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("seller", "0001_initial"),
        ("product", "0011_alter_product_created_at"),
    ]

    operations = [
        migrations.CreateModel(
            name="Kupon",
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
                ("name", models.CharField(max_length=300)),
                (
                    "kupon_discount",
                    models.IntegerField(
                        validators=[django.core.validators.MaxValueValidator(100)]
                    ),
                ),
                ("expire_date", models.DateTimeField()),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.product",
                    ),
                ),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="seller.profile"
                    ),
                ),
            ],
        ),
    ]
