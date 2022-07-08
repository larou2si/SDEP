# Generated by Django 4.0.1 on 2022-02-07 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appServers', '0002_remove_server_project_server_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(blank=True, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='server',
            name='port',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]