# Generated by Django 4.2.6 on 2023-10-24 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_rename_personaloan_personalloan'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalloan',
            name='loan_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
