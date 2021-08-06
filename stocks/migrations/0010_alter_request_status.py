# Generated by Django 3.2 on 2021-08-06 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0009_request_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('p', 'Pending'), ('a', 'Accepted'), ('c', 'Cancelled')], default='p', max_length=10),
        ),
    ]
