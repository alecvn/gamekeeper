# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-31 22:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamekeeper.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allocation', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='N/A', max_length=128)),
                ('beneficiary', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gamekeeper.Player')),
                ('point', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamekeeper.Point')),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='players',
            field=models.ManyToManyField(to='gamekeeper.Player'),
        ),
        migrations.AddField(
            model_name='match',
            name='rules',
            field=models.ManyToManyField(to='gamekeeper.Rule'),
        ),
        migrations.AddField(
            model_name='game',
            name='rules',
            field=models.ManyToManyField(to='gamekeeper.Rule'),
        ),
        migrations.AddField(
            model_name='event',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamekeeper.Game'),
        ),
        migrations.AddField(
            model_name='event',
            name='players',
            field=models.ManyToManyField(to='gamekeeper.Player'),
        ),
        migrations.AddField(
            model_name='event',
            name='rules',
            field=models.ManyToManyField(to='gamekeeper.Rule'),
        ),
    ]