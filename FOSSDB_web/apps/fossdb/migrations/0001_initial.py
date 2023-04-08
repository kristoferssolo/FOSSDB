# Generated by Django 4.1.7 on 2023-04-08 12:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HostingPlatform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hosting_platform', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=50)),
                ('full_name', models.CharField(blank=True, default='', max_length=100)),
                ('url', models.URLField(blank=True, default='')),
                ('description', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='ProgrammingLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, default='')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, default='')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='types/icons/')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectProgrammingLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.PositiveIntegerField()),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fossdb.programminglanguage')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fossdb.project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectHostingPlatform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('hosting_platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fossdb.hostingplatform')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fossdb.project')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='hosting_platform',
            field=models.ManyToManyField(related_name='projects', through='fossdb.ProjectHostingPlatform', to='fossdb.hostingplatform'),
        ),
        migrations.AddField(
            model_name='project',
            name='licenses',
            field=models.ManyToManyField(to='fossdb.license'),
        ),
        migrations.AddField(
            model_name='project',
            name='programming_languages',
            field=models.ManyToManyField(related_name='projects', through='fossdb.ProjectProgrammingLanguage', to='fossdb.programminglanguage'),
        ),
        migrations.AddField(
            model_name='project',
            name='project_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fossdb.tag'),
        ),
    ]
