# Generated by Django 5.0.8 on 2024-08-29 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0008_renthistory_total_price_alter_renthistory_created_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='renthistory',
            name='total_price',
        ),
    ]
