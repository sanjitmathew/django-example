# Generated by Django 3.2.5 on 2021-12-26 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_userinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='pic',
            field=models.ImageField(blank=True, upload_to='media/pics'),
        ),
    ]
