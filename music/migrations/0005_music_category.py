# Generated by Django 4.1.7 on 2023-04-05 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("music", "0004_category_alter_music_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="music",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="music.category",
            ),
        ),
    ]
