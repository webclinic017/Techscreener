# Generated by Django 3.2.7 on 2021-09-17 04:11

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Strategy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buy', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, size=None)),
                ('sell', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, size=None)),
                ('name', models.CharField(help_text='Name of our strategy', max_length=50)),
                ('length', models.IntegerField(help_text='Number of items to be looped over')),
            ],
            options={
                'db_table': 'strategy',
            },
        ),
    ]
