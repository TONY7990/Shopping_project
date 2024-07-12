# Generated by Django 5.0.6 on 2024-06-14 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_cartitem_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=255)),
                ('place', models.CharField(max_length=255)),
                ('paymenttype', models.IntegerField(default=0)),
            ],
        ),
    ]
