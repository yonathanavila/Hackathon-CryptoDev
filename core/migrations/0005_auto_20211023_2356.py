# Generated by Django 3.1.2 on 2021-10-24 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20211023_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poaplink',
            name='linkpoap',
            field=models.FileField(blank=True, db_column='linkpoaps', null=True, upload_to='poap/%Y/%m/%d', verbose_name='Links POAPS'),
        ),
    ]