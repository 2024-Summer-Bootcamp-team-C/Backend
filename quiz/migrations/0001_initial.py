# Generated by Django 5.0.6 on 2024-07-03 06:28

import jsonfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('quizId', models.AutoField(primary_key=True, serialize=False)),
                ('question', jsonfield.fields.JSONField()),
                ('answer', jsonfield.fields.JSONField()),
                ('explanation', jsonfield.fields.JSONField()),
            ],
        ),
    ]
