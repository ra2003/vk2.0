# Generated by Django 2.1.5 on 2019-03-10 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0036_groupmessages_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='dialog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='account.Dialog'),
        ),
    ]
