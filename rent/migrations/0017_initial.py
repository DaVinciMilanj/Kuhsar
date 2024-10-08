# Generated by Django 5.0.8 on 2024-08-31 08:32

import django.db.models.deletion
import django_jalali.db.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rent', '0016_remove_rentroom_user_delete_renthistory_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RentHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField(blank=True)),
                ('paid', models.BooleanField(default=False)),
                ('total_price', models.PositiveBigIntegerField(blank=True, null=True)),
                ('created', django_jalali.db.models.jDateTimeField(auto_now_add=True)),
                ('paid_change', django_jalali.db.models.jDateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_history', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RentRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField()),
                ('start_date', django_jalali.db.models.jDateField()),
                ('end_date', django_jalali.db.models.jDateField()),
                ('best_date', django_jalali.db.models.jDateField()),
                ('detail', models.TextField(blank=True, null=True)),
                ('golden_date', django_jalali.db.models.jDateField(blank=True)),
                ('discount', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('paid', models.BooleanField(default=False)),
                ('create', django_jalali.db.models.jDateTimeField(auto_now_add=True)),
                ('update', django_jalali.db.models.jDateTimeField(auto_now=True)),
                ('user', models.ForeignKey(limit_choices_to={'status': 'owner'}, on_delete=django.db.models.deletion.CASCADE, related_name='user_rent', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
