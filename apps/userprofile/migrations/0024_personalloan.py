# Generated by Django 3.0.7 on 2022-02-14 17:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0023_auto_20220214_1125'),
    ]

    operations = [
        migrations.CreateModel(
            name='personalloan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=12)),
                ('lastname', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=150)),
                ('phone_number', models.CharField(blank=True, max_length=12)),
                ('income', models.IntegerField(blank=True, max_length=12, validators=[django.core.validators.MinValueValidator(25000)])),
                ('gender', models.CharField(max_length=1)),
                ('MARITAL_STATUS', models.CharField(max_length=6)),
                ('loan_type', models.CharField(default='Personal_loan', max_length=13)),
            ],
        ),
    ]
