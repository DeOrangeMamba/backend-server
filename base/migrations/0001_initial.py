# Generated by Django 4.0.6 on 2022-08-05 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airline_companies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('image', models.ImageField(blank=True, default='/placeholder.png', null=True, upload_to='static')),
            ],
        ),
        migrations.CreateModel(
            name='Flights',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Departure_Time', models.DateTimeField()),
                ('Landing_Time', models.DateTimeField()),
                ('Remaining_Tickets', models.IntegerField()),
                ('Airline_Company_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.airline_companies')),
                ('Destination_Country_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Destination', to='base.country')),
                ('Origin_Country_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Origin', to='base.country')),
            ],
        ),
        migrations.CreateModel(
            name='User_Roles',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Roles_Name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Userr',
            fields=[
                ('Username', models.TextField(max_length=18, unique=True)),
                ('Password', models.TextField(max_length=18)),
                ('Email', models.TextField(max_length=50, unique=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('User_Role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.user_roles')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.userr')),
                ('Flight_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.flights')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.TextField(max_length=13)),
                ('LastName', models.TextField(max_length=18)),
                ('Adress', models.TextField(max_length=18)),
                ('PhoneNumber', models.TextField(max_length=14)),
                ('Credit_Card_Number', models.TextField(max_length=30, unique=True)),
                ('User_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.userr')),
            ],
        ),
        migrations.AddField(
            model_name='airline_companies',
            name='Country_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.country'),
        ),
        migrations.AddField(
            model_name='airline_companies',
            name='User_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.userr'),
        ),
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.TextField(max_length=13)),
                ('LastName', models.TextField(max_length=18)),
                ('User_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.userr')),
            ],
        ),
    ]
