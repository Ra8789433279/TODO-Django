# Generated by Django 4.2.9 on 2024-02-27 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="tasks",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tasksTitle", models.CharField(max_length=30)),
                ("tasksDesc", models.TextField()),
                ("time", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
