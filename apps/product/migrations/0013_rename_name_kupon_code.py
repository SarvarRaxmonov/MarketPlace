# Generated by Django 4.2.1 on 2023-08-23 14:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0012_kupon"),
    ]

    operations = [
        migrations.RenameField(
            model_name="kupon",
            old_name="name",
            new_name="code",
        ),
    ]
