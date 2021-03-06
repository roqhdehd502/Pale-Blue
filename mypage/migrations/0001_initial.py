# Generated by Django 3.2.3 on 2021-06-05 16:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0006_alter_post_options'),
        ('photo', '0003_auto_20210520_2254'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='PROFILE')),
            ],
        ),
        migrations.CreateModel(
            name='MyCommunity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.post', verbose_name='COMMUNITY')),
            ],
            options={
                'ordering': ('community',),
            },
        ),
        migrations.CreateModel(
            name='MyAlbum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='photo.album', verbose_name='ALBUM')),
            ],
            options={
                'ordering': ('album',),
            },
        ),
    ]
