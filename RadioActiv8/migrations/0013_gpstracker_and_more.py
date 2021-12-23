# Generated by Django 4.0 on 2021-12-23 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RadioActiv8', '0012_patrol_attendance_points_patrol_bonus_points_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='GPSTracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eui', models.CharField(max_length=16)),
                ('name', models.CharField(max_length=32, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='intelligence_answered_correctly',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='patrol',
            name='gps_tracker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='RadioActiv8.gpstracker'),
        ),
    ]
