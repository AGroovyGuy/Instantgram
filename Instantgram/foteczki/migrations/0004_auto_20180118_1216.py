# Generated by Django 2.0.1 on 2018-01-18 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foteczki', '0003_auto_20180118_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='home/konrad/Pulpit/Instantgram/Instantgram/foteczki'),
        ),
    ]