# Generated by Django 3.2.12 on 2022-08-16 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EventsApp', '0059_alter_organization_postal_code'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cart',
            new_name='OrderItems',
        ),
    ]