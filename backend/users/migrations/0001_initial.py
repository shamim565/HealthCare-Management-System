# Generated by Django 5.1.7 on 2025-03-15 06:58

import users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('email_confirmed_at', models.DateTimeField(null=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('phone_number', models.CharField(max_length=20, null=True, unique=True)),
                ('phone_number_confirmed_at', models.DateTimeField(null=True)),
                ('date_of_birth', models.DateField(null=True)),
                ('gender', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('OTHERS', 'Others')], max_length=20, null=True)),
                ('picture', models.ImageField(null=True, upload_to='profile_pictures/')),
                ('address', models.CharField(max_length=255, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('role', models.SmallIntegerField(choices=[(0, 'Admin'), (1, 'Doctor'), (2, 'Nurse'), (3, 'Patient'), (4, 'Receptionist')], default=3)),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ('-id',),
            },
            managers=[
                ('objects', users.models.UserManager()),
            ],
        ),
    ]
