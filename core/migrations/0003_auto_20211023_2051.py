# Generated by Django 3.1.2 on 2021-10-24 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_poaplink'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poaplink',
            name='link_poap',
        ),
        migrations.AddField(
            model_name='poaplink',
            name='linkpoap',
            field=models.FileField(blank=True, db_column='linkpoaps', null=True, upload_to='poap/%Y/%m/%d', verbose_name='Links POAPS'),
        ),
    ]