# Generated by Django 4.1.3 on 2023-11-28 09:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalPerformance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('on_time_delivery_rate', models.FloatField()),
                ('quality_rating_avg', models.FloatField()),
                ('average_response_time', models.FloatField()),
                ('fulfillment_rate', models.FloatField()),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor_api.vendor')),
            ],
        ),
    ]