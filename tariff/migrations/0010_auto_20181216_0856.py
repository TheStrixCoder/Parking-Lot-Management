# Generated by Django 2.1.4 on 2018-12-16 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tariff', '0009_auto_20181216_0852'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_type', models.CharField(choices=[('Hour', 'Hour ticket')], max_length=20, verbose_name='Billing type')),
                ('per_hour_money', models.FloatField(default=10.0, verbose_name='Hourly parking fee')),
            ],
            options={
                'verbose_name': 'Tickets',
                'verbose_name_plural': 'Tickets',
            },
        ),
        migrations.AddField(
            model_name='tariffs',
            name='ticket_type',
            field=models.CharField(choices=[('Hour', 'Hour ticket')], default='hour', max_length=20, verbose_name='Billing type'),
        ),
    ]
