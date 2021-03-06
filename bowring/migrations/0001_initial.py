# Generated by Django 3.0.3 on 2020-09-16 14:37

import bowring.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=150)),
                ('is_active', models.BooleanField(default=True, help_text='利用状況フラグ\u30001:利用中 0:利用不可')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_user_id', models.IntegerField()),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('updated_user_id', models.IntegerField()),
                ('is_deleted', models.IntegerField(default=0)),
                ('deleted_at', models.DateTimeField()),
                ('deleted_user_id', models.IntegerField()),
            ],
            options={
                'db_table': 'user',
            },
            managers=[
                ('objects', bowring.models.CustomUserManager()),
            ],
        ),
    ]
