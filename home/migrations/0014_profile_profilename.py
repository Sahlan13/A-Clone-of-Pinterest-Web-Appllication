# Generated by Django 4.2.4 on 2023-11-07 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_rename_image_board_image1_board_image2_board_image3'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profilename',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
