# Generated by Django 2.2.4 on 2020-09-20 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0022_car_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='feature_expire',
            field=models.DateField(blank=True, null=True),
        ),
    ]