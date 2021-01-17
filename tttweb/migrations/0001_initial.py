# Generated by Django 3.1.5 on 2021-01-17 19:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(verbose_name='date created')),
                ('updated', models.DateTimeField(verbose_name='date updated')),
                ('name', models.CharField(max_length=200)),
                ('board_text', models.CharField(max_length=200)),
                ('player', models.IntegerField(default=0)),
                ('player0', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player0', to=settings.AUTH_USER_MODEL)),
                ('player1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player1', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
