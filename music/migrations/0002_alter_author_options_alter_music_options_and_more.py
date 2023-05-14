# Generated by Django 4.1.7 on 2023-04-02 20:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("music", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="author",
            options={
                "verbose_name": "Исполнитель",
                "verbose_name_plural": "Исполнители",
            },
        ),
        migrations.AlterModelOptions(
            name="music",
            options={"verbose_name": "Песня", "verbose_name_plural": "Песни"},
        ),
        migrations.AlterField(
            model_name="author",
            name="name",
            field=models.CharField(max_length=50, verbose_name="Имя исполнителя"),
        ),
        migrations.AlterField(
            model_name="music",
            name="audio",
            field=models.FileField(upload_to="uploads/%Y/%m/%d/", verbose_name="Песня"),
        ),
        migrations.AlterField(
            model_name="music",
            name="name",
            field=models.CharField(max_length=100, verbose_name="Название"),
        ),
    ]