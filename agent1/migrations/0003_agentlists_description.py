# Generated by Django 5.1.3 on 2024-11-15 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent1', '0002_alter_agentlists_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='agentlists',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
