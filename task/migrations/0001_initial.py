# Generated by Django 4.1.4 on 2022-12-23 16:42

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
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_new', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('date_published', models.DateTimeField()),
                ('content_html', models.CharField(max_length=255)),
                ('summery', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
