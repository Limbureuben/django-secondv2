# Generated by Django 5.1.6 on 2025-03-20 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_alter_reporthistory_report_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reporthistory',
            name='report_id',
            field=models.CharField(blank=True, max_length=8),
        ),
    ]
