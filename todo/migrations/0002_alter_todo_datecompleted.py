# Generated by Django 4.2 on 2023-06-28 11:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todo", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="datecompleted",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
