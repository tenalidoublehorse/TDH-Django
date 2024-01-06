# Generated by Django 4.2.6 on 2024-01-06 11:09

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndusData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Firstname', models.CharField(max_length=50)),
                ('Lastname', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('Phonenumber', models.IntegerField()),
                ('PurposeofContact', models.CharField(blank=True, max_length=50, null=True)),
                ('Message', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('AddedTimeStamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('updatedTimeStamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
