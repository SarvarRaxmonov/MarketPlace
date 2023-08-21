# Generated by Django 4.2.1 on 2023-08-21 15:31

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("seller", "0001_initial"),
        ("product", "0004_alter_product_wholesale"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="profile",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="seller.profile",
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="main_category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="categories",
                to="product.maincategory",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="discount",
            field=models.PositiveIntegerField(
                validators=[django.core.validators.MaxValueValidator(100)]
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="review_product",
                to="product.product",
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="rate",
            field=models.PositiveIntegerField(
                validators=[django.core.validators.MaxValueValidator(5)]
            ),
        ),
    ]
