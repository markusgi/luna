# Generated by Django 3.1.2 on 2020-10-28 16:46

import apps.registration.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=apps.registration.models.code_generator, help_text='random code used for registration and for password reset', max_length=15, verbose_name='code')),
                ('code_type', models.CharField(choices=[('RV', 'Registration Validation'), ('PR', 'Password Reset')], max_length=2, verbose_name='code type')),
                ('code_used', models.BooleanField(default=False, verbose_name='code used')),
            ],
        ),
    ]
