# Generated by Django 3.0.8 on 2020-12-20 16:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('itjob', '0006_remove_vacancy_apply_before'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='apply_before',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='published_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
