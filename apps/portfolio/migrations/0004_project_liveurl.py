# Generated by Django 3.2.7 on 2021-09-07 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20210907_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='liveurl',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
