# Generated by Django 2.1.7 on 2019-03-25 09:42

from django.db import migrations, models
import django.db.models.deletion
import django_thumbs.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_catalogitems_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail_Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail_title', models.CharField(help_text='Наименование товара', max_length=200)),
                ('detail_img', django_thumbs.fields.ImageThumbsField(default='', help_text='Изображения товара', sizes=({'code': 'resized', 'resize': 'crop', 'wxh': '800x400'},), upload_to='main/img/detail_img/')),
                ('detail_description', models.TextField(default='')),
                ('detail_cost', models.FloatField(default=0)),
                ('slug', models.SlugField(default='slug')),
            ],
        ),
        migrations.RemoveField(
            model_name='catalogitems',
            name='slug',
        ),
        migrations.AddField(
            model_name='detail_items',
            name='detail_cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.CatalogItems'),
        ),
    ]
