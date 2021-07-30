# Generated by Django 3.2.5 on 2021-07-30 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_alter_bid_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='status',
            field=models.CharField(choices=[('Unsold', 'Unsold'), ('Sold', 'Sold')], default='Unsold', max_length=200),
        ),
    ]
