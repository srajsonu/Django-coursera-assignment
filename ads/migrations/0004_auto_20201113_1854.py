# Generated by Django 3.1.3 on 2020-11-13 18:54

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ads', '0003_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(5, 'Title must be greater than 5 characters')])),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('comments', models.ManyToManyField(related_name='forum_comments', through='ads.Comment', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forums_owned', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='forum',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.forum'),
        ),
    ]