# Generated by Django 4.0 on 2021-12-23 00:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RadioActiv8', '0010_base_attendance_points_base_repeatable_base_run_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patrol',
            name='current_base',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='RadioActiv8.base'),
        ),
    ]