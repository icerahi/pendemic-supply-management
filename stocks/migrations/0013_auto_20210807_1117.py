# Generated by Django 3.2 on 2021-08-07 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0012_auto_20210806_1459'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='equipment',
            options={'verbose_name': ' Equipment'},
        ),
        migrations.AlterModelOptions(
            name='request',
            options={'ordering': ['-created'], 'verbose_name': '  Equipment Request'},
        ),
        migrations.AlterModelOptions(
            name='stock',
            options={'ordering': ['-updated'], 'verbose_name': 'Equipments Stock'},
        ),
    ]