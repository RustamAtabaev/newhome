# Generated by Django 2.1.7 on 2019-03-25 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_catalog_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogitems',
            name='catalog_same',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Catalog', verbose_name='Категория'),
        ),
    ]