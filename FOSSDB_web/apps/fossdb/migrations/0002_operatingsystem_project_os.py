# Generated by Django 4.1.7 on 2023-04-09 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fossdb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OperatingSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, default='')),
                ('version', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='os',
            field=models.ManyToManyField(to='fossdb.operatingsystem'),
        ),
    ]
