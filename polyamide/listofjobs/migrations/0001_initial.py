# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='joblisting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hiring_position_text', models.CharField(max_length=50)),
                ('hiring_industry_text', models.CharField(max_length=50)),
                ('posting_publish_date', models.DateTimeField(verbose_name=b'date published')),
                ('hiring_description_md', models.CharField(max_length=2000)),
                ('hiring_primary_location', models.CharField(max_length=2000)),
                ('posting_id', models.PositiveIntegerField()),
            ],
        ),
    ]
