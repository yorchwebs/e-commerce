from django.db import models


# Create your models here.
class Role(models.Model):
    id_rol = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "roles"


class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.last_name}"

    class Meta:
        db_table = "users"
