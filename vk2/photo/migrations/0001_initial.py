# Generated by Django 2.1.5 on 2019-03-19 08:07

import account.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0057_auto_20190319_1507'),
        ('post', '0002_auto_20190319_1507'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_photo', models.IntegerField(null=True, unique=True)),
                ('photo', models.ImageField(blank=True, default='defult-photo.png', null=True, upload_to=account.models.user_directory_path)),
                ('like_put', models.BooleanField(default=False, null=True)),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='account.Account')),
                ('post', models.ManyToManyField(blank=True, related_name='images', to='post.Post')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
