# Generated by Django 4.2.5 on 2023-10-05 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USER_PROFILE', '0003_remove_profile_user_alter_profile_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, default='images/default.png', null=True, upload_to='img'),
        ),
    ]
