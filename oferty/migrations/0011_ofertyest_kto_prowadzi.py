# Generated by Django 2.1.2 on 2018-12-03 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oferty', '0010_ofertyusers'),
    ]

    operations = [
        migrations.AddField(
            model_name='ofertyest',
            name='kto_prowadzi',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
