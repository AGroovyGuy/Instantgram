# Generated by Django 2.0.1 on 2018-01-18 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foteczki', '0004_auto_20180118_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(default=1, upload_to='home/konrad/Pulpit/Instantgram/Instantgram/foteczki/images'),
            preserve_default=False,
        ),
    ]
