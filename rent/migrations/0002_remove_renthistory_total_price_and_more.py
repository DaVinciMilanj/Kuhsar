# Generated by Django 5.0.7 on 2024-08-12 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='renthistory',
            name='total_price',
        ),
        migrations.AlterField(
            model_name='rentroom',
            name='discount',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
