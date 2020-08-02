# Generated by Django 2.2.11 on 2020-08-01 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oferty', '0015_ofertyest_data_sprz'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomOffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('token', models.CharField(max_length=8)),
                ('ip', models.GenericIPAddressField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomOfferId',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oferty.OfertyEst')),
            ],
        ),
    ]
