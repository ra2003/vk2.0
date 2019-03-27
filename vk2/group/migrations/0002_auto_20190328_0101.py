# Generated by Django 2.1.5 on 2019-03-27 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('post', '0001_initial'),
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='fixed_post',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='_group', to='post.Post'),
        ),
        migrations.AddField(
            model_name='group',
            name='subscribers',
            field=models.ManyToManyField(blank=True, related_name='group', to='account.Account'),
        ),
    ]