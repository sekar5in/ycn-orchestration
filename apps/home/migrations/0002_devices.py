# Generated by Django 3.2.13 on 2022-06-09 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='devices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deviceName', models.CharField(max_length=255)),
                ('deviceIPAddr', models.GenericIPAddressField()),
                ('deviceSerial', models.CharField(max_length=255)),
                ('deviceLocation', models.CharField(max_length=255)),
                ('deviceSite', models.CharField(max_length=255)),
                ('deviceDesc', models.CharField(max_length=255)),
                ('deviceType', models.CharField(max_length=10)),
                ('devicePort', models.IntegerField()),
                ('deviceLogin', models.CharField(max_length=15)),
                ('devicePassword', models.CharField(max_length=15)),
                ('deviceOrg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.org')),
            ],
        ),
    ]