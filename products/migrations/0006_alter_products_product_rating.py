# Generated by Django 3.2.3 on 2021-06-27 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20210627_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_rating',
            field=models.FloatField(blank=True, editable=False, null=True),
        ),
    ]
