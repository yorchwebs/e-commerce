from django.db import models
from users.models import User
from products.models import Product


# Create your models here.
class Favourite(models.Model):
    id_favourite = models.AutoField(primary_key=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE
    )  # Suponiendo que un usuario solo puede tener un producto favorito
    product = models.OneToOneField(
        Product, on_delete=models.CASCADE
    )  # Suponiendo que un producto puede ser favorito de un solo usuario

    def __str__(self):
        return f"{self.user} favours {self.product}"

    class Meta:
        db_table = "favourites"
