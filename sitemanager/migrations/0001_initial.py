# Generated by Django 2.2 on 2019-04-06 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sitemanager',
            fields=[
                ('user_name', models.CharField(default='', max_length=15, verbose_name='username')),
                ('user_phone', models.CharField(default='', max_length=10, verbose_name='cellphone number')),
                ('site_no', models.IntegerField(default=0, primary_key=True, serialize=False, verbose_name='site number')),
                ('is_manager', models.BooleanField(default=False, verbose_name='Admin Bit')),
            ],
            options={
                'verbose_name': 'Site Manager Info',
                'verbose_name_plural': 'Site Manager Info',
            },
        ),
    ]
