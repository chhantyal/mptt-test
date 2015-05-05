# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageProxy',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('app.page',),
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='app.Page')),
                ('quote', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('app.pageproxy',),
        ),
    ]
