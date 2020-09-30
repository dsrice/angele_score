# Generated by Django 3.1.1 on 2020-09-30 15:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bowring', '0002_auto_20200917_0026'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_user_id', models.IntegerField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('updated_user_id', models.IntegerField(blank=True, null=True)),
                ('is_deleted', models.IntegerField(default=0)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_user_id', models.IntegerField(blank=True, null=True)),
                ('event_date', models.DateTimeField()),
                ('name', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'events',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_user_id', models.IntegerField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('updated_user_id', models.IntegerField(blank=True, null=True)),
                ('is_deleted', models.IntegerField(default=0)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_user_id', models.IntegerField(blank=True, null=True)),
                ('total_score', models.IntegerField()),
                ('base_score', models.IntegerField()),
                ('total_handicap', models.IntegerField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bowring.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'results',
            },
        ),
        migrations.CreateModel(
            name='GameScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_user_id', models.IntegerField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('updated_user_id', models.IntegerField(blank=True, null=True)),
                ('is_deleted', models.IntegerField(default=0)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_user_id', models.IntegerField(blank=True, null=True)),
                ('game_count', models.IntegerField()),
                ('score', models.IntegerField()),
                ('base_score', models.IntegerField()),
                ('handicap', models.IntegerField()),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bowring.result')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'game_scores',
            },
        ),
        migrations.CreateModel(
            name='FrameScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_user_id', models.IntegerField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('updated_user_id', models.IntegerField(blank=True, null=True)),
                ('is_deleted', models.IntegerField(default=0)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_user_id', models.IntegerField(blank=True, null=True)),
                ('frame_count', models.IntegerField()),
                ('frame_type', models.IntegerField()),
                ('frame_score', models.IntegerField()),
                ('gamescore', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bowring.gamescore')),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bowring.result')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'frame_scores',
            },
        ),
        migrations.CreateModel(
            name='FramePin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_user_id', models.IntegerField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('updated_user_id', models.IntegerField(blank=True, null=True)),
                ('is_deleted', models.IntegerField(default=0)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_user_id', models.IntegerField(blank=True, null=True)),
                ('pin1', models.BooleanField()),
                ('pin2', models.BooleanField()),
                ('pin3', models.BooleanField()),
                ('pin4', models.BooleanField()),
                ('pin5', models.BooleanField()),
                ('pin6', models.BooleanField()),
                ('pin7', models.BooleanField()),
                ('pin8', models.BooleanField()),
                ('pin9', models.BooleanField()),
                ('pin10', models.BooleanField()),
                ('framescore', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bowring.framescore')),
                ('gamescore', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bowring.gamescore')),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bowring.result')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'frame_pins',
            },
        ),
    ]
