# Generated by Django 4.1.7 on 2024-02-12 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("ddpui", "0042_orgtask_generated_by_task_is_system"),
    ]

    operations = [
        migrations.CreateModel(
            name="OrgDbtModel",
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
                ("name", models.CharField(max_length=100)),
                ("display_name", models.CharField(max_length=100)),
                ("sql_path", models.CharField(max_length=200, null=True)),
                ("config", models.JSONField(null=True)),
                (
                    "orgdbt",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ddpui.orgdbt"
                    ),
                ),
            ],
        ),
    ]
