# Generated by Django 4.0.1 on 2022-02-08 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appServers', '0005_remove_box_project_server_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='box',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appServers.box'),
        ),
        migrations.AlterField(
            model_name='server',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appServers.project'),
        ),
    ]
