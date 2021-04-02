# Generated by Django 3.0.3 on 2020-03-10 11:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classifier', '0002_remove_messages_reciever'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='reciever',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]