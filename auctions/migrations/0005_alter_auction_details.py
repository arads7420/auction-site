# Generated by Django 3.2.5 on 2021-07-27 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_alter_auction_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='details',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
