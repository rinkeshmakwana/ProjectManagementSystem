# Generated by Django 3.0.7 on 2020-06-27 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='emp_type',
            field=models.CharField(choices=[('1', 'Developer'), ('2', 'Team Lead'), ('3', 'Project Manager')], default=1, max_length=3),
        ),
    ]
