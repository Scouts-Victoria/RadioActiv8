# Generated by Django 4.0.5 on 2022-07-01 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoutsvic_extranet', '0004_historicalmemberclass_priority_memberclass_priority'),
        ('RadioActiv8', '0024_historicalpatrol_member_class_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalpatrol',
            name='member_class',
        ),
        migrations.RemoveField(
            model_name='patrol',
            name='member_class',
        ),
        migrations.AddField(
            model_name='patrol',
            name='member_classes',
            field=models.ManyToManyField(blank=True, to='scoutsvic_extranet.memberclass'),
        ),
    ]
