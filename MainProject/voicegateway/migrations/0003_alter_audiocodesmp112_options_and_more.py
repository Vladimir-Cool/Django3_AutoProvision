# Generated by Django 4.1.6 on 2023-03-09 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voicegateway', '0002_audiocodesmp112_typeaudiocodesmp112_delete_test_gw_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='audiocodesmp112',
            options={'verbose_name': 'AudiocodesMP112', 'verbose_name_plural': 'AudiocodesMP112s'},
        ),
        migrations.AlterModelOptions(
            name='typeaudiocodesmp112',
            options={'verbose_name': 'TypeAudiocodesMP112', 'verbose_name_plural': 'TypeAudiocodesMP112s'},
        ),
        migrations.AlterField(
            model_name='audiocodesmp112',
            name='login1',
            field=models.CharField(max_length=20, null=True, verbose_name='Логин 1 порта'),
        ),
        migrations.AlterField(
            model_name='audiocodesmp112',
            name='login2',
            field=models.CharField(max_length=20, null=True, verbose_name='Логин 2 порта'),
        ),
        migrations.AlterField(
            model_name='audiocodesmp112',
            name='password1',
            field=models.CharField(max_length=20, null=True, verbose_name='Пароль 1 порта'),
        ),
        migrations.AlterField(
            model_name='audiocodesmp112',
            name='password2',
            field=models.CharField(max_length=20, null=True, verbose_name='Пароль 2 порта'),
        ),
    ]
