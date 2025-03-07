# Generated by Django 3.2.12 on 2022-12-21 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventsApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='city',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='country',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='province',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='geographical_scope',
            field=models.CharField(blank=True, choices=[('Local', 'Local'), ('Provincial', 'Provincial'), ('National', 'National')], max_length=100, null=True),
        ),
    ]
