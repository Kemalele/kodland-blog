# Generated by Django 3.1 on 2020-08-07 10:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('image', models.ImageField(upload_to='userImages')),
            ],
        ),
    ]
