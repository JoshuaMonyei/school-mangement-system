# Generated by Django 4.1.4 on 2023-01-22 11:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('school_management', '0004_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
