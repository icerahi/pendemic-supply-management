from django.db import models
from django.conf import settings
from django.db.models.fields import BooleanField
# Create your models here.


class Stock(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="equipment")
    quantity = models.PositiveIntegerField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Equipments Stock'
        ordering = ['-updated']


class Request(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    equipment = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    message = models.TextField()
    accepted = BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.equipment.name

    class Meta:
        verbose_name = 'Equipment Request'
        ordering = ['-created']
