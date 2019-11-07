# Generated by Django 2.1.3 on 2018-11-06 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tariff', '0003_rates_site_add'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tariffs',
            options={'verbose_name': 'Tariffs Center', 'verbose_name_plural': 'Tariffs center'},
        ),
        migrations.AlterModelOptions(
            name='tickets',
            options={'verbose_name': 'Tickets', 'verbose_name_plural': 'Tickets'},
        ),
        migrations.AddField(
            model_name='tariffs',
            name='postion_no',
            field=models.CharField(default='Not Parked', max_length=20, verbose_name='Parking Site Number'),
        ),
        migrations.AddField(
            model_name='tariffs',
            name='site_address',
            field=models.CharField(default='Not Parked', max_length=20, verbose_name='Site Address'),
        ),
        migrations.AlterField(
            model_name='tariffs',
            name='end_time',
            field=models.DateTimeField(null=True, verbose_name='Out-Time'),
        ),
        migrations.AlterField(
            model_name='tariffs',
            name='parking_money',
            field=models.FloatField(default=0.0, editable=False, verbose_name='Bill Amount'),
        ),
        migrations.AlterField(
            model_name='tariffs',
            name='per_hour_money',
            field=models.FloatField(default=0.0, verbose_name='Parking fees'),
        ),
        migrations.AlterField(
            model_name='tariffs',
            name='start_time',
            field=models.DateTimeField(null=True, verbose_name='In-Time'),
        ),
    ]
