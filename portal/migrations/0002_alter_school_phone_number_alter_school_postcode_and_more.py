# Generated by Django 4.0.3 on 2022-03-28 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='phone_number',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='postcode',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='school_website',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='town',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.CharField(max_length=200, null=True, verbose_name='Date of birth'),
        ),
    ]
