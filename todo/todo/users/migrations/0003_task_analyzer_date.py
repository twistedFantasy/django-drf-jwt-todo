# Generated by Django 2.1.5 on 2019-01-10 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='analyzer_date',
            field=models.DateField(blank=True, null=True, verbose_name='Analyzer Date'),
        ),
    ]