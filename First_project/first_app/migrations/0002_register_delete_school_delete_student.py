# Generated by Django 4.2.2 on 2023-07-01 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=400)),
            ],
        ),
        migrations.DeleteModel(
            name='School',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
