# Generated by Django 4.0.6 on 2022-08-05 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_roles',
            name='Roles_Name',
        ),
        migrations.AddField(
            model_name='user_roles',
            name='role',
            field=models.CharField(choices=[('CR', 'Customer'), ('AC', 'Companies'), ('MR', 'Manager')], default='CR', max_length=2),
        ),
    ]
