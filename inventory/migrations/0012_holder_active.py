# Generated by Django 2.1.1 on 2018-10-08 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_asset_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='holder',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
