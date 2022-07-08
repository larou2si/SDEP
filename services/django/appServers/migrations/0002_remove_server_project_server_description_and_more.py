# Generated by Django 4.0.1 on 2022-02-06 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appServers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='server',
            name='project',
        ),
        migrations.AddField(
            model_name='server',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='server',
            name='is_product',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='server',
            name='is_sidbar',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('project', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='appServers.project')),
            ],
            options={
                'db_table': 'box',
            },
        ),
    ]