# Generated by Django 3.2.10 on 2021-12-31 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websiteapp1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pediaobject',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
