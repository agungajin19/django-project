# Generated by Django 3.0 on 2019-12-10 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=200)),
                ('isi', models.CharField(default='', max_length=400)),
                ('foto', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Mentee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(default='', max_length=200)),
                ('foto', models.CharField(max_length=300)),
                ('quote', models.CharField(default='', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200)),
                ('foto', models.CharField(max_length=300)),
                ('quote', models.CharField(default='', max_length=300)),
                ('experience', models.CharField(default='', max_length=300)),
            ],
        ),
    ]
