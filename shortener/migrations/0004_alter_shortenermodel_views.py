# Generated by Django 4.1.7 on 2023-04-03 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0003_alter_shortenermodel_encoded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortenermodel',
            name='views',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]