# Generated by Django 3.2.3 on 2021-06-29 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('description', models.TextField()),
                ('api', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.IntegerField()),
                ('product_pieces', models.IntegerField()),
                ('buyers', models.IntegerField()),
                ('payment_method', models.CharField(max_length=50)),
                ('invoice_request', models.TextField()),
                ('invoice_create_date', models.DateTimeField(auto_now_add=True)),
                ('invoice_status', models.CharField(max_length=25)),
                ('invoice_price', models.FloatField()),
                ('invoice_status_time', models.JSONField()),
                ('invoice_courier', models.IntegerField()),
                ('invoice_receipt_number', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('description', models.TextField()),
                ('api', models.JSONField()),
            ],
        ),
    ]
