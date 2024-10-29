from django.db import models
from users.models import User


# Create your models here.
class Direction(models.Model):
    id_direction = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}, {self.country}"

    class Meta:
        db_table = "directions"
