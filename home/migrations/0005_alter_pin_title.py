# Generated by Django 4.2.4 on 2023-11-03 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_pin_board_pin_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]