# Generated by Django 4.2.6 on 2023-10-24 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_personalloan_loan_start'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalloan',
            name='loan_type',
            field=models.CharField(choices=[('personal', 'personal'), ('business', 'business')], default='personal', max_length=20),
        ),
    ]
