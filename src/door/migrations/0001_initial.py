# Generated by Django 3.2.2 on 2021-05-09 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Door',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('door_name', models.CharField(max_length=50, null=True)),
                ('door_type', models.CharField(max_length=30)),
            ],
        ),
    ]
