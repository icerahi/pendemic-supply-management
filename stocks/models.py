from django.db import models
from django.conf import settings
from django.utils.safestring import mark_safe
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.contrib.auth import get_user_model
from django.contrib import messages
# Create your models here.
User = get_user_model()


class Equipment(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to="equipment_img")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '  Equipment'

    @mark_safe
    def image_tag(self):
        if self.image:
            return '<a href="{}"><img src="{}" style="width: 30px; height:30px;" /></a>'.format(self.image.url, self.image.url)
        else:
            return 'No Image Found'

    image_tag.short_description = 'Image'


class Stock(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.equipment.name

    class Meta:
        verbose_name = ' Equipments Stock'
        ordering = ['-updated']
        unique_together = ("user", "equipment")
        # constraints = [
        #     models.UniqueConstraint(
        #         fields=['user', 'equipment', ],
        #         name="Can't create multiple stock of same equipment,So update the existing equipment's quantity"
        #     ),
        # ]

    @mark_safe
    def image_tag(self):
        if self.equipment.image:
            return '<a href="{}"><img src="{}" style="width: 30px; height:30px;" /></a>'.format(self.equipment.image.url, self.equipment.image.url)
        else:
            return 'No Image Found'

    image_tag.short_description = 'Image'


class Request(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    message = models.TextField()
  
    status   = models.CharField(max_length=10,default='p',choices=(('p','Pending'),('a','Accepted'),('d','Delivered'),('c','Cancelled')))

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.equipment.name

    class Meta:
        verbose_name = 'Equipment Request'
        ordering = ['-created']

    @mark_safe
    def image_tag(self):
        if self.equipment.image:
            return '<a href="{}"><img src="{}" style="width: 30px; height:30px;" /></a>'.format(self.equipment.image.url, self.equipment.image.url)
        else:
            return 'No Image Found'

    image_tag.short_description = 'Image'
