# Generated by Django 2.2.4 on 2020-09-20 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0024_auto_20200920_0535'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='premium_feature_count',
            field=models.IntegerField(blank=True, default='0', null=True),
        ),
    ]
