# Generated by Django 3.2 on 2021-07-28 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tea_App', '0003_black_tea_fermented_tea_green_tea_herbal_tea_matcha_tea_oolong_tea_white_tea'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='black_tea',
            name='first_section',
        ),
        migrations.RemoveField(
            model_name='black_tea',
            name='second_section',
        ),
        migrations.RemoveField(
            model_name='fermented_tea',
            name='first_section',
        ),
        migrations.RemoveField(
            model_name='fermented_tea',
            name='second_section',
        ),
        migrations.RemoveField(
            model_name='green_tea',
            name='first_section',
        ),
        migrations.RemoveField(
            model_name='green_tea',
            name='second_section',
        ),
        migrations.RemoveField(
            model_name='herbal_tea',
            name='first_section',
        ),
        migrations.RemoveField(
            model_name='herbal_tea',
            name='second_section',
        ),
        migrations.RemoveField(
            model_name='matcha_tea',
            name='first_section',
        ),
        migrations.RemoveField(
            model_name='matcha_tea',
            name='second_section',
        ),
        migrations.RemoveField(
            model_name='oolong_tea',
            name='first_section',
        ),
        migrations.RemoveField(
            model_name='oolong_tea',
            name='second_section',
        ),
        migrations.RemoveField(
            model_name='white_tea',
            name='first_section',
        ),
        migrations.RemoveField(
            model_name='white_tea',
            name='second_section',
        ),
    ]
