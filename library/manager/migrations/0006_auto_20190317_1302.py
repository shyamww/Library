# Generated by Django 2.1.7 on 2019-03-17 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_auto_20190316_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='BookPDF',
            field=models.FileField(blank=True, null=True, upload_to='manger/book/pdf/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='CoverPicture',
            field=models.ImageField(blank=True, null=True, upload_to='manager/book/coverPic/%Y/%m/%d/'),
        ),
    ]