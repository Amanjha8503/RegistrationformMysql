# Generated by Django 4.2.2 on 2023-06-29 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstproject', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Regg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=7)),
                ('college', models.CharField(max_length=15)),
            ],
        ),
    ]
