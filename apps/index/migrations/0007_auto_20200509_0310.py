# Generated by Django 3.0.5 on 2020-05-09 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_remove_user_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='fio',
            field=models.CharField(default='user', max_length=100)
        ),
    ]