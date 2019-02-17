# Generated by Django 2.1.7 on 2019-02-14 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_items_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Identity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identity', models.TextField(help_text='uniq identity')),
            ],
        ),
        migrations.AddField(
            model_name='items',
            name='identity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Identity'),
        ),
    ]
