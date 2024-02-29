# Generated by Django 4.1.5 on 2023-03-10 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0007_alter_adminreg_admin_password'),
        ('Guest', '0007_rename_landload_vstatue_landload_landload_vstatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plot_des', models.CharField(max_length=50)),
                ('plot_image', models.FileField(upload_to='userdocs/')),
                ('plot_amount', models.IntegerField(default=0)),
                ('Landload_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Guest.landload')),
                ('location_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Admin.location')),
            ],
        ),
    ]