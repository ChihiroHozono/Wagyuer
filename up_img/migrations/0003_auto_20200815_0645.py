# Generated by Django 2.2.12 on 2020-08-15 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('up_img', '0002_wagyupackageimgpath'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WagyuPackageImgPath',
            new_name='WagyuPackageImg',
        ),
        migrations.RenameField(
            model_name='wagyupackageimg',
            old_name='img_path',
            new_name='img',
        ),
    ]