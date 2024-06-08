# Generated by Django 5.0.6 on 2024-06-07 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_no', models.IntegerField()),
                ('month', models.CharField(max_length=20)),
                ('no_of_days_present', models.IntegerField()),
            ],
            options={
                'db_table': 'employee_attendance',
            },
        ),
    ]
