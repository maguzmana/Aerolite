# Generated by Django 4.2.1 on 2023-06-25 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Usuario",
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
                ("nombre", models.CharField(max_length=100)),
                ("correo", models.EmailField(max_length=254)),
                ("direccion", models.CharField(max_length=200)),
                ("telefono", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Ventilador",
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
                ("nombre", models.CharField(max_length=100)),
                ("descripcion", models.TextField()),
                ("imagen", models.ImageField(upload_to="ventiladores/")),
                ("precio", models.DecimalField(decimal_places=2, max_digits=8)),
                ("stock", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Venta",
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
                ("fecha_venta", models.DateTimeField(auto_now_add=True)),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.usuario"
                    ),
                ),
                (
                    "ventilador",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.ventilador",
                    ),
                ),
            ],
        ),
    ]
