# Generated by Django 2.1.7 on 2019-03-23 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oferty', '0013_auto_20190323_1351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ofertyest',
            name='pdf',
        ),
    ]
