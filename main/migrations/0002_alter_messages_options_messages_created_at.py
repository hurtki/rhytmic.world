# Generated by Django 5.1.6 on 2025-02-11 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='messages',
            options={'verbose_name': 'Сообщение', 'verbose_name_plural': 'Сообщения'},
        ),
        migrations.AddField(
            model_name='messages',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
