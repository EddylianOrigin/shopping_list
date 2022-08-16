from ssl import create_default_context
from unicodedata import name
from django.db import models
from datetime import date
# Create your models here.


class ShoppingItem(models.Model):
    created_at = models.DateField(default=date.today)
    name = models.CharField(max_length=200)
    done = models.BooleanField(default=False)

    def __str__(self):
        # return super().__str__()
        return str(self.id) + ' ' + self.name
