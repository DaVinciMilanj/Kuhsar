# Generated by Django 5.0.7 on 2024-08-12 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeuser',
            name='status',
            field=models.CharField(blank=True, choices=[('admin', 'admin'), ('owner', 'owner'), ('customer', 'customer')], max_length=18, null=True),
        ),
    ]
