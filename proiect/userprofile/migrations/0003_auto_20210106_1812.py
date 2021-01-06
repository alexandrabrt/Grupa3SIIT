# Generated by Django 3.1 on 2021-01-06 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_logs'),
    ]

    operations = [
        migrations.AddField(
            model_name='logs',
            name='url',
            field=models.CharField(default=1, max_length=100, verbose_name='URL'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='logs',
            name='action',
            field=models.CharField(choices=[('created', 'created'), ('updated', 'updated'), ('refresh', 'refresh')], max_length=10, verbose_name='Action'),
        ),
    ]
