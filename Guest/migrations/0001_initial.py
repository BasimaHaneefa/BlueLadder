# Generated by Django 4.1.5 on 2023-02-03 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0005_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('user_contact', models.CharField(max_length=10)),
                ('user_email', models.EmailField(max_length=254, unique=True)),
                ('user_address', models.TextField(null=True)),
                ('user_photo', models.FileField(upload_to='userdocs/')),
                ('user_proof', models.FileField(upload_to='userdocs/')),
                ('user_pswrd', models.CharField(max_length=50, unique=True)),
                ('user_doj', models.DateField(auto_now=True)),
                ('user_location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Admin.location')),
            ],
        ),
    ]
