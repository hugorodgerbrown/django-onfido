# Generated by Django 3.1.3 on 2021-05-05 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("onfido", "0017_auto_20210304_0241"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="check",
            name="is_clear",
        ),
        migrations.RemoveField(
            model_name="report",
            name="is_clear",
        ),
    ]
