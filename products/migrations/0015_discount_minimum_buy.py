# Generated by Django 3.2.3 on 2021-06-29 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20210629_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='minimum_buy',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
