# Generated by Django 3.2.13 on 2022-06-08 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Org',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org', models.CharField(max_length=255)),
                ('orgId', models.CharField(max_length=255)),
            ],
        ),
    ]