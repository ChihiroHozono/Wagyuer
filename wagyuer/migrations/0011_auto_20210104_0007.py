# Generated by Django 3.1.4 on 2021-01-03 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagyuer', '0010_auto_20210103_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wagyuinfomation',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='出生日'),
        ),
        migrations.AlterField(
            model_name='wagyuinfomation',
            name='slaughter_date',
            field=models.DateField(blank=True, null=True, verbose_name='と畜日'),
        ),
    ]