# Generated by Django 2.2.6 on 2019-10-20 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0006_metadata_thumb'),
    ]

    operations = [
        migrations.AddField(
            model_name='metadata',
            name='day',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='metadata',
            name='thumb',
            field=models.ImageField(upload_to='', verbose_name=models.ImageField(default='assets', upload_to='blah')),
        ),
    ]
