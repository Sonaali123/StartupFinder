# Generated by Django 5.1.2 on 2024-11-06 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StartupProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('website_url', models.URLField(blank=True)),
                ('skills_required', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('logo', models.ImageField(blank=True, upload_to='logos/')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('country', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('projects', models.TextField(blank=True)),
                ('skills', models.TextField(blank=True)),
                ('experience', models.TextField(blank=True)),
                ('interests', models.TextField(blank=True)),
                ('address', models.CharField(max_length=255)),
                ('phone_number', models.CharField(blank=True, max_length=20)),
            ],
        ),
    ]
