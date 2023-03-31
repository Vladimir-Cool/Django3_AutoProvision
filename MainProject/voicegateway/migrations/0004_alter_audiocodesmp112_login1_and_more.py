# Generated by Django 4.1.6 on 2023-03-09 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voicegateway', '0003_alter_audiocodesmp112_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiocodesmp112',
            name='login1',
            field=models.CharField(default='login1', max_length=20, verbose_name='Логин 1 порта'),
        ),
        migrations.AlterField(
            model_name='audiocodesmp112',
            name='login2',
            field=models.CharField(default='login2', max_length=20, verbose_name='Логин 2 порта'),
        ),
        migrations.AlterField(
            model_name='audiocodesmp112',
            name='password1',
            field=models.CharField(default='pass1', max_length=20, verbose_name='Пароль 1 порта'),
        ),
        migrations.AlterField(
            model_name='audiocodesmp112',
            name='password2',
            field=models.CharField(default='pass2', max_length=20, verbose_name='Пароль 2 порта'),
        ),
    ]