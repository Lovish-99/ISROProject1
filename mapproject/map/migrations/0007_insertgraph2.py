# Generated by Django 3.2.6 on 2021-09-08 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0006_auto_20210908_1924'),
    ]

    operations = [
        migrations.CreateModel(
            name='insertgraph2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service1', models.CharField(max_length=300)),
                ('service2', models.CharField(max_length=300)),
                ('service3', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'insertgraph2',
            },
        ),
    ]
