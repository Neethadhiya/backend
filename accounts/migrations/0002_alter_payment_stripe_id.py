# Generated by Django 4.2.5 on 2023-11-25 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='stripe_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
