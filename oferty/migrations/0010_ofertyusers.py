# Generated by Django 2.1.2 on 2018-12-03 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oferty', '0009_ofertybiuro_nazwisko'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfertyUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('fullname', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('phone2', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('email2', models.CharField(max_length=30)),
                ('fullname_gen', models.CharField(max_length=30)),
                ('fullname_respons', models.CharField(max_length=30)),
                ('license', models.CharField(max_length=30)),
                ('license2', models.CharField(max_length=30)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
