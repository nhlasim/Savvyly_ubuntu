# Generated by Django 4.2.6 on 2023-10-25 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_alter_personalloan_loan_status_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PersonalLoan',
        ),
    ]
