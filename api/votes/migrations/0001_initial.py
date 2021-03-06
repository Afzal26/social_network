# Generated by Django 3.2.6 on 2021-08-30 16:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(choices=[(1, 'Up'), (-1, 'Down')])),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_votes', to='posts.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_votes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_related_name': 'post_votes',
                'unique_together': {('post', 'user')},
            },
        ),
    ]
