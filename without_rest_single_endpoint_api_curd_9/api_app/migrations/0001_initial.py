# Generated by Django 4.2.2 on 2023-09-07 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('eno', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('esal', models.FloatField()),
            ],
        ),
    ]
