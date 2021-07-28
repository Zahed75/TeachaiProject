# Generated by Django 3.2 on 2021-07-28 06:51

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_me_avatar', models.ImageField(upload_to='about_me_picture')),
                ('about_me_description', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='ImageSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_img', models.ImageField(upload_to='slider_images')),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SiteUtilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_us_avatar', models.ImageField(upload_to='site_utilities', verbose_name='Please put your about us profile pic')),
                ('about_us_description', ckeditor.fields.RichTextField()),
                ('help_text', ckeditor.fields.RichTextField()),
                ('home_first_section_heading', ckeditor.fields.RichTextField()),
                ('home_second_section_heading', ckeditor.fields.RichTextField()),
                ('types_heading', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subs_mail', models.EmailField(max_length=300)),
                ('subs_first_name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='TypesOfTea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tea_picture', models.ImageField(upload_to='tea_types')),
                ('type_name', models.CharField(max_length=100, null=True)),
                ('tea_description', ckeditor.fields.RichTextField()),
                ('first_section', models.BooleanField(default=False)),
                ('second_section', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('blog', ckeditor.fields.RichTextField()),
                ('thumbnail_img', models.ImageField(upload_to='blog_thumbnails')),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
