# Generated by Django 4.2.1 on 2023-08-20 14:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="WholesalePartner",
            new_name="WholeSale",
        ),
        migrations.AlterField(
            model_name="category",
            name="image",
            field=models.FileField(upload_to="category_images/"),
        ),
        migrations.AlterField(
            model_name="maincategory",
            name="image",
            field=models.FileField(upload_to="main_category_images/"),
        ),
        migrations.AlterField(
            model_name="product",
            name="condition",
            field=models.CharField(
                choices=[
                    ("refurbished", "Refurbished"),
                    ("brand_new", "Brand New"),
                    ("old_items", "Old Items"),
                ],
                max_length=40,
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="currency",
            field=models.CharField(
                choices=[
                    ("USD", "US Dollar"),
                    ("EUR", "Euro"),
                    ("GBP", "British Pound"),
                ],
                max_length=40,
            ),
        ),
    ]