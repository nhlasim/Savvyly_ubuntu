# Generated by Django 4.2.6 on 2023-10-12 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_kyc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kyc',
            name='identity_type',
            field=models.CharField(choices=[('national_id_card', 'National ID Card'), ('drivers_licence', 'Drivers Licence'), ('international_passport', 'International Passport')], max_length=140),
        ),
    ]