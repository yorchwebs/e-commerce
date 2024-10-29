from django.db import models
from users.models import User
from products.models import Product
from shipping.models import Direction


# Create your models here.
class Order(models.Model):
    id_order = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
    date_order = models.DateTimeField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    state = models.CharField(max_length=255)

    def __str__(self):
        return f"Order {self.id_order} by {self.user}"

    class Meta:
        db_table = "orders"


class OrderDetail(models.Model):
    id_detail = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    unite_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Detail for Order {self.order.id_order}: {self.product.name}"

    class Meta:
        db_table = "order_details"

