# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-12 11:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Baccalaureat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('school_origin', models.CharField(max_length=100)),
                ('bac_year', models.CharField(max_length=4)),
                ('table_number', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=45)),
                ('country_code', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.CharField(max_length=16)),
                ('baccalaureat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Baccalaureat')),
            ],
        ),
        migrations.CreateModel(
            name='StudentDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('detail_high_school', models.CharField(max_length=45)),
                ('details_last_modified', models.DateField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Country')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
        ),
    ]
