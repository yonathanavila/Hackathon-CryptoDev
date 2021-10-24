# Generated by Django 3.1.2 on 2021-10-24 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20211023_2356'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(db_column='Link', default=None, max_length=5000, null=True)),
            ],
            options={
                'db_table': 'Link',
            },
        ),
    ]
