# Generated by Django 3.1.4 on 2021-01-03 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagyuer', '0011_auto_20210104_0007'),
    ]

    operations = [
        migrations.AddField(
            model_name='wagyuinfomation',
            name='wagyu_package',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='wagyuer.wagyupackageimg'),
            preserve_default=False,
        ),
    ]
