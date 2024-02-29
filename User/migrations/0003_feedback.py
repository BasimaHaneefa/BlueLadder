# Generated by Django 4.1.5 on 2023-02-25 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0007_rename_landload_vstatue_landload_landload_vstatus'),
        ('User', '0002_complaint'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_description', models.TextField(null=True)),
                ('feedback_date', models.DateField(auto_now=True)),
                ('Landload_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Guest.landload')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Guest.userregistration')),
                ('worker_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Guest.worker')),
            ],
        ),
    ]
