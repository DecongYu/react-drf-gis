# Generated by Django 3.2.7 on 2022-06-10 02:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_alter_profile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.UUIDField(default=uuid.UUID('a457b711-4b30-4aba-b485-890f56cdd121'), editable=False, unique=True),
        ),
    ]
