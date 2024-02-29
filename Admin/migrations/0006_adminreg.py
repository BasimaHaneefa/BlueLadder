# Generated by Django 4.1.5 on 2023-02-17 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0005_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminReg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_name', models.CharField(max_length=50)),
                ('admin_email', models.EmailField(max_length=254, unique=True)),
                ('admin_password', models.CharField(max_length=50)),
            ],
        ),
    ]