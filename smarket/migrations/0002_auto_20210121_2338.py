# Generated by Django 3.1.5 on 2021-01-22 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smarket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='nome',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
