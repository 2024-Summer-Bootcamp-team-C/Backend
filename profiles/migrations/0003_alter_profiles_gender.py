# Generated by Django 5.0.6 on 2024-07-03 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profiles_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='gender',
            field=models.CharField(max_length=10),
        ),
    ]
