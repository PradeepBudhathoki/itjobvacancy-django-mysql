# Generated by Django 3.0.8 on 2020-12-21 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itjob', '0009_auto_20201221_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='apply_before',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='req_no',
            field=models.IntegerField(null=True),
        ),
    ]
