# Generated by Django 2.1.5 on 2019-03-10 11:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0035_groupmessages_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupmessages',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
