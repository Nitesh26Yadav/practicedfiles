# Generated by Django 4.1.5 on 2023-01-03 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='favoriteItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite_item_name', models.CharField(max_length=200)),
                ('favorite_item_desc', models.CharField(max_length=200)),
                ('favorite_item_price', models.IntegerField()),
                ('favorite_item_quantity', models.IntegerField()),
            ],
        ),
    ]
