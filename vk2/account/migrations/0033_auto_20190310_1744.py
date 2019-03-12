# Generated by Django 2.1.5 on 2019-03-10 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0032_auto_20190310_0008'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupMassages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dialog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='group_massages', to='account.Dialog')),
            ],
        ),
        migrations.RemoveField(
            model_name='massage',
            name='dialog',
        ),
        migrations.AddField(
            model_name='massage',
            name='group_massages',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='massages', to='account.GroupMassages'),
        ),
    ]
