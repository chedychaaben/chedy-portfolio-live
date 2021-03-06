# Generated by Django 3.2.7 on 2021-09-07 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_rename_priview_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='images',
            field=models.ManyToManyField(blank=True, to='portfolio.ProjectImage'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='image',
            field=models.FileField(upload_to='skills/'),
        ),
    ]
