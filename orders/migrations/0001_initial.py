# Generated by Django 5.1.2 on 2024-10-29 20:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("products", "0001_initial"),
        ("shipping", "0001_initial"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                ("id_order", models.AutoField(primary_key=True, serialize=False)),
                ("date_order", models.DateTimeField()),
                ("total", models.DecimalField(decimal_places=2, max_digits=10)),
                ("state", models.CharField(max_length=255)),
                (
                    "direction",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shipping.direction",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.user"
                    ),
                ),
            ],
            options={
                "db_table": "orders",
            },
        ),
        migrations.CreateModel(
            name="OrderDetail",
            fields=[
                ("id_detail", models.AutoField(primary_key=True, serialize=False)),
                ("amount", models.IntegerField()),
                ("unite_price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="orders.order"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                    ),
                ),
            ],
            options={
                "db_table": "order_details",
            },
        ),
    ]
