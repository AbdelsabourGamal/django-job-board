# Generated by Django 5.1.3 on 2025-02-10 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_job_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
