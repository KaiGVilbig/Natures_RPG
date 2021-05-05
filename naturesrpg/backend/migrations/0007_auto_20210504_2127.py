# Generated by Django 3.2 on 2021-05-04 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_player_num_of_obs'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='profile_pic',
            field=models.CharField(default='https://www.pngitem.com/pimgs/m/30-307416_profile-icon-png-image-free-download-searchpng-employee.png', max_length=150),
        ),
        migrations.AlterField(
            model_name='observation',
            name='image_link',
            field=models.CharField(default='https://www.pngitem.com/pimgs/m/30-307416_profile-icon-png-image-free-download-searchpng-employee.png', max_length=150),
        ),
    ]
