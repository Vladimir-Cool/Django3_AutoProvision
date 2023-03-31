# Generated by Django 4.1.6 on 2023-03-17 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voicegateway', '0008_alter_loginpasswordgw_unique_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='maingateway',
            options={'ordering': ['name_gw'], 'verbose_name': 'Голосовой шлюз', 'verbose_name_plural': 'Голосовые шлюзы'},
        ),
        migrations.AlterModelOptions(
            name='typegateway',
            options={'ordering': ['name_type'], 'verbose_name': 'Таблица типов голосовых шлюзов', 'verbose_name_plural': 'Таблицы типов голосовых шлюзов'},
        ),
        migrations.AddField(
            model_name='typegateway',
            name='template_file',
            field=models.FileField(default='-', max_length=50, upload_to=''),
        ),
        migrations.AlterField(
            model_name='maingateway',
            name='ip',
            field=models.GenericIPAddressField(unique=True),
        ),
        migrations.AlterField(
            model_name='maingateway',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='voicegateway.typegateway'),
        ),
    ]