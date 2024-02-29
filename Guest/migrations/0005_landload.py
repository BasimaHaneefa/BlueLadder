# Generated by Django 4.1.5 on 2023-02-16 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0005_location'),
        ('Guest', '0004_remove_worker_place_id_worker_location_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Landload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('landload_name', models.CharField(max_length=50)),
                ('landload_address', models.TextField(null=True)),
                ('landload_contact', models.CharField(max_length=10)),
                ('landload_email', models.EmailField(max_length=254, unique=True)),
                ('landload_photo', models.FileField(upload_to='userdocs/')),
                ('landload_password', models.CharField(max_length=50, unique=True)),
                ('landload_proof', models.FileField(upload_to='userdocs/')),
                ('landload_vstatue', models.IntegerField(default=0)),
                ('landload_doj', models.DateField(auto_now=True)),
                ('location_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Admin.location')),
            ],
        ),
    ]