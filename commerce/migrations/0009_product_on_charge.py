# Generated by Django 3.2.8 on 2021-12-19 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0008_auto_20211219_0841'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='on_charge',
            field=models.BooleanField(default=bool, verbose_name='on charge'),
            preserve_default=False,
        ),
    ]
