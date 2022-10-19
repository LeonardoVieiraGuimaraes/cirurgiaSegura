# Generated by Django 4.1 on 2022-10-18 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DadosUsuario",
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
                ("usuario", models.CharField(max_length=50)),
                ("dataNascimento", models.DateField()),
                ("prontuario", models.CharField(max_length=50)),
                ("nomeMae", models.CharField(max_length=50)),
            ],
        ),
    ]
