# Generated by Django 5.0.6 on 2024-07-15 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list_task', '0003_alter_task_date_creation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(max_length=13),
        ),
    ]
