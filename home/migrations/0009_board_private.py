# Generated by Django 4.2.4 on 2023-11-06 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_board_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='private',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
