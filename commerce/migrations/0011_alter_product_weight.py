# Generated by Django 3.2.8 on 2021-12-20 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0010_auto_20211219_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=10, null=True, verbose_name='weight'),
        ),
    ]
