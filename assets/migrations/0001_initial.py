# Generated by Django 3.0.4 on 2020-03-17 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServerInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('networkType', models.CharField(default='cloud', max_length=30, verbose_name='networkType')),
                ('cloudServerProvider', models.CharField(blank=True, max_length=30, verbose_name='cloudServerProvider')),
                ('serverName', models.CharField(blank=True, max_length=100, null=True, verbose_name='serverName')),
                ('osVersion', models.CharField(blank=True, max_length=100, null=True, verbose_name='osVersion')),
                ('publicIP', models.GenericIPAddressField(blank=True, null=True, protocol='IPv4', verbose_name='publicIP')),
                ('privateIP', models.GenericIPAddressField(blank=True, null=True, protocol='IPv4', verbose_name='privateIP')),
                ('owner', models.CharField(blank=True, max_length=50, null=True, verbose_name='owner')),
            ],
            options={
                'verbose_name': '服务器信息',
                'verbose_name_plural': '服务器信息',
            },
        ),
    ]
