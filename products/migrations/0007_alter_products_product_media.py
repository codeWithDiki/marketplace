# Generated by Django 3.2.3 on 2021-06-27 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_products_product_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_media',
            field=models.JSONField(blank=True, editable=False, null=True),
        ),
    ]
