# Generated by Django 3.2.3 on 2021-05-27 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(max_length=20, null=True, verbose_name='CATEGORY'),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(blank=True, help_text='내용을 입력하세요.', max_length=100, verbose_name='DESCRIPTION'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(allow_unicode=True, help_text='해당 별칭을 지정하세요.', unique=True, verbose_name='SLUG'),
        ),
    ]