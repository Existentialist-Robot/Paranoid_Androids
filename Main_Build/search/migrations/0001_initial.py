# Generated by Django 2.2.5 on 2019-10-19 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('slug', models.SlugField()),
                ('body', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('thumb', models.ImageField(blank=True, default='default.png', upload_to='')),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]