# Generated by Django 3.0.7 on 2020-07-17 16:09

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EndGemapp', '0005_uploadfolder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfolder',
            name='File_to_upload',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/media/subject1'), upload_to=''),
        ),
    ]