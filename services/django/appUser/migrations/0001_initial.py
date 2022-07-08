# Generated by Django 3.2.8 on 2021-11-08 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('image', models.ImageField(default='defaultprofile.jpg', upload_to='profile_pics')),
                ('email_confirmed', models.BooleanField(default=False)),
                ('domains', models.TextField(blank=True, null=True)),
                ('etats', models.TextField(blank=True, null=True)),
                ('headers', models.TextField(blank=True, null=True)),
                ('subdomains', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
