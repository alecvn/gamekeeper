# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-04 23:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gamekeeper', '0008_outcome'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='outcome',
            name='action',
        ),
        migrations.RemoveField(
            model_name='outcome',
            name='event',
        ),
        migrations.RemoveField(
            model_name='outcome',
            name='player',
        ),
        migrations.AlterField(
            model_name='action',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_actions', to='gamekeeper.Action'),
        ),
        migrations.AlterField(
            model_name='player',
            name='actions',
            field=models.ManyToManyField(blank=True, to='gamekeeper.Action'),
        ),
        migrations.AlterField(
            model_name='player',
            name='points',
            field=models.ManyToManyField(blank=True, to='gamekeeper.Point'),
        ),
        migrations.DeleteModel(
            name='Outcome',
        ),
        migrations.AddField(
            model_name='result',
            name='action',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='gamekeeper.Action'),
        ),
        migrations.AddField(
            model_name='result',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='gamekeeper.Event'),
        ),
        migrations.AddField(
            model_name='result',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='gamekeeper.Player'),
        ),
    ]
