# Generated by Django 2.1.7 on 2019-03-01 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20190228_1556'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='catalog',
            options={'ordering': ['catalog_order'], 'verbose_name': 'Категории', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AddField(
            model_name='catalog',
            name='catalog_order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
