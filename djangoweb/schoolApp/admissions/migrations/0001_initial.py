# Generated by Django 3.1.4 on 2021-09-05 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('fathername', models.CharField(max_length=20)),
                ('classname', models.IntegerField()),
                ('contact', models.CharField(max_length=20)),
            ],
        ),
    ]
