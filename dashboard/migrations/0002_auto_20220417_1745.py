# Generated by Django 2.2.27 on 2022-04-17 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='elephant',
            old_name='identifier',
            new_name='id',
        ),
        migrations.AlterField(
            model_name='elephant',
            name='event',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
