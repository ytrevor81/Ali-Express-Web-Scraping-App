# Generated by Django 3.0.1 on 2019-12-27 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alisubmission',
            name='epacket',
        ),
        migrations.AddField(
            model_name='alisubmission',
            name='search',
            field=models.CharField(default='BLANK', max_length=250),
        ),
        migrations.AddField(
            model_name='alisubmission',
            name='shipping',
            field=models.CharField(default='-', max_length=10),
        ),
        migrations.AlterField(
            model_name='alisubmission',
            name='price',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='alisubmission',
            name='rating',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='alisubmission',
            name='sold',
            field=models.CharField(max_length=10),
        ),
    ]
