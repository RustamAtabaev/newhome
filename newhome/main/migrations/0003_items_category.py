# Generated by Django 2.1.7 on 2019-02-14 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='category',
            field=models.ManyToManyField(help_text='Choose category', to='main.Category'),
        ),
    ]
