# Generated by Django 3.2.12 on 2022-11-21 18:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EventsApp', '0077_auto_20220912_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='master_table',
            name='datetimes_all',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_time', models.DateTimeField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('header', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('scope', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.TextField(blank=True, null=True)),
                ('url', models.TextField(blank=True, null=True)),
                ('hit_count', models.IntegerField(blank=True, null=True)),
                ('max_hits', models.IntegerField(blank=True, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]