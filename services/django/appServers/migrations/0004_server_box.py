# Generated by Django 4.0.1 on 2022-02-07 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appServers', '0003_alter_project_name_alter_server_port'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='box',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='appServers.box'),
            preserve_default=False,
        ),
    ]
