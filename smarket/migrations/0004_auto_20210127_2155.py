# Generated by Django 3.1.5 on 2021-01-28 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smarket', '0003_auto_20210122_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='nome',
            field=models.CharField(max_length=50),
        ),
    ]
