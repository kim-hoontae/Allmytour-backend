# Generated by Django 3.2.6 on 2021-09-24 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneCheck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=45)),
                ('auth_number', models.IntegerField()),
                ('expired_at', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'phone_checks',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=300, null=True)),
                ('phone_number', models.CharField(max_length=45)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='UserTemp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=300, null=True)),
                ('code', models.CharField(max_length=30)),
                ('expired_at', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'user_temp',
            },
        ),
    ]
