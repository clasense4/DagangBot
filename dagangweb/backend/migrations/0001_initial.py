# Generated by Django 2.1.4 on 2018-12-13 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(null=True)),
                ('price', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(null=True)),
                ('telegram_id', models.TextField(null=True)),
                ('first_name', models.TextField(null=True)),
                ('last_name', models.TextField(null=True)),
                ('register_date', models.TextField(null=True)),
            ],
        ),
    ]