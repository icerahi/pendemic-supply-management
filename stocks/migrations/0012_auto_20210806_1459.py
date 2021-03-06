# Generated by Django 3.2 on 2021-08-06 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0011_auto_20210806_1151'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='stock',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='stock',
            constraint=models.UniqueConstraint(fields=('user', 'equipment'), name="Can't create multiple stock of same equipment,So update the existing equipment's quantity"),
        ),
    ]
