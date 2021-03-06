# Generated by Django 3.2 on 2021-07-28 17:51

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tea_App', '0004_auto_20210728_1318'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderAndFooter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disclaimer_text', ckeditor.fields.RichTextField(verbose_name='Put your footer disclaimer section text here')),
                ('footer_under_logo_text', ckeditor.fields.RichTextField(verbose_name='Put your footer under logo text here')),
                ('facebook_link', models.URLField(max_length=500, verbose_name='Your facebook account link')),
                ('youtube_link', models.URLField(max_length=500, verbose_name='Your youtube account link')),
                ('linkedin_link', models.URLField(max_length=500, verbose_name='Your linkedIn account link')),
                ('twitter_link', models.URLField(max_length=500, verbose_name='Your twitter account link')),
                ('dribble_link', models.URLField(max_length=500, verbose_name='Your dribble account link')),
                ('instagram_link', models.URLField(max_length=500, verbose_name='Your instagram account link')),
            ],
        ),
    ]
