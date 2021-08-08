from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Asset(models.Model):
    name = models.TextField()
    model = models.TextField()
    memory = models.IntegerField()
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    issuer = models.TextField()
    asset_user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    is_active = models.BooleanField(default=True)
