# Generated by Django 4.2.6 on 2023-10-24 08:28

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0005_alter_account_user_personaloan'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PersonaLoan',
            new_name='PersonalLoan',
        ),
    ]