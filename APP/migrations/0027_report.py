# Generated by Django 2.2.4 on 2020-09-21 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0026_car_features'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
                ('reason', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
