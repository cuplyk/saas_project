# Generated by Django 5.0.14 on 2025-05-02 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("visits", "0004_pagevisit_page"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pagevisit",
            name="page",
            field=models.TextField(blank=True, null=True),
        ),
    ]
