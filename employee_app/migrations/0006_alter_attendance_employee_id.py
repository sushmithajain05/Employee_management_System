# Generated by Django 5.0.6 on 2024-07-15 12:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0005_attendance_alter_employee_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='employee_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='employee_app.employee'),
        ),
    ]
