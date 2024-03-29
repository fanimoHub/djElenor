# Generated by Django 4.2.10 on 2024-02-29 08:12

import djElenor.permission.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('codename', models.CharField(max_length=100, verbose_name='codename')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content_type', to='contenttypes.contenttype', verbose_name='content type')),
            ],
            options={
                'verbose_name': 'permission',
                'verbose_name_plural': 'permissions',
                'ordering': ['content_type__app_label', 'content_type__model', 'codename'],
                'unique_together': {('content_type', 'codename')},
            },
            managers=[
                ('objects', djElenor.permission.models.PermissionManager()),
            ],
        ),
    ]
