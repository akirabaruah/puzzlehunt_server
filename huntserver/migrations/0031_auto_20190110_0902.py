# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-10 14:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('huntserver', '0030_prepuzzle_released'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prepuzzle',
            name='template',
            field=models.TextField(default='{% extends "prepuzzle.html" %}\r\n{% load prepuzzle_tags %}\r\n\r\n{% block content %}\r\n{% endblock content %}', help_text=b'The template string to be rendered to HTML on the hunt page'),
        ),
    ]