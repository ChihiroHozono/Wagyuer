# Generated by Django 3.1.4 on 2021-01-03 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagyuer', '0006_auto_20210103_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wagyupackageimg',
            name='upload_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
