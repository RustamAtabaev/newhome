# Generated by Django 2.1.7 on 2019-02-28 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_recomend'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='RelatedModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rel_category', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='mymodel',
            name='related_fk',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='main.RelatedModel', verbose_name='Related Lookup (FK)'),
        ),
    ]