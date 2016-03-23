# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-22 18:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=255, verbose_name='username')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('city', models.CharField(max_length=60)),
                ('user_status', models.PositiveSmallIntegerField(choices=[(1, 'volunteer'), (2, 'recipant')])),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_name', models.CharField(max_length=120)),
                ('material_message', models.TextField()),
                ('material_image', models.ImageField(upload_to=b'')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'not_rezerved'), (1, 'rezerved'), (2, 'given')])),
                ('given_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='material_given_to', to=settings.AUTH_USER_MODEL)),
                ('reserved_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='material_reserved_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('message', models.TextField()),
                ('release_date', models.DateTimeField(auto_now=True)),
                ('unpublishing_date', models.DateTimeField(auto_now_add=True)),
                ('is_accomplished', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PostConfirmation',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='comodo.Post')),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_added', to=settings.AUTH_USER_MODEL)),
                ('approved_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_approved', to=settings.AUTH_USER_MODEL)),
            ],
            bases=('comodo.post',),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
