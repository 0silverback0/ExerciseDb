# Generated by Django 4.2.7 on 2023-11-27 03:51

import articles.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('date', models.DateField(default=articles.models.get_current_date, editable=False)),
                ('text', models.TextField()),
            ],
        ),
    ]
