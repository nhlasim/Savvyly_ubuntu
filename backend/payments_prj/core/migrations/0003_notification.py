# Generated by Django 4.2.6 on 2023-10-15 16:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_creditcard'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_type', models.CharField(choices=[('None', 'None'), ('Transfer', 'Transfer'), ('Credit Alert', 'Credit Alert'), ('Debit Alert', 'Debit Alert'), ('Sent Payment Request', 'Sent Payment Request'), ('Recieved Payment Request', 'Recieved Payment Request'), ('Funded Credit Card', 'Funded Credit Card'), ('Withdrew Credit Card Funds', 'Withdrew Credit Card Funds'), ('Deleted Credit Card', 'Deleted Credit Card'), ('Added Credit Card', 'Added Credit Card')], default='none', max_length=100)),
                ('amount', models.IntegerField(default=0)),
                ('is_read', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('nid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvxyz', length=10, max_length=25, prefix='')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Notification',
                'ordering': ['-date'],
            },
        ),
    ]