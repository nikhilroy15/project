# Generated by Django 3.2.5 on 2022-11-23 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjects', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=50)),
                ('fee', models.IntegerField()),
            ],
        ),
    ]
