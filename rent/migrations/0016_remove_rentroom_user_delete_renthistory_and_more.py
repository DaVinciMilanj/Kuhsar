# Generated by Django 5.0.8 on 2024-08-31 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0015_alter_rentroom_end_date_alter_rentroom_start_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rentroom',
            name='user',
        ),
        migrations.DeleteModel(
            name='RentHistory',
        ),
        migrations.DeleteModel(
            name='RentRoom',
        ),
    ]
