# Generated by Django 3.2.6 on 2021-09-08 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0005_alter_insertgraph_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='insertgraph',
            name='serv2',
        ),
        migrations.RemoveField(
            model_name='insertgraph',
            name='serv3',
        ),
        migrations.AlterModelTable(
            name='insertgraph',
            table=None,
        ),
    ]
