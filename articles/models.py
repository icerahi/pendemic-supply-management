from django.db import models
from django.db.models.fields.files import ImageField

# Create your models here.

class Article(models.Model):
    title   = models.CharField(max_length=300)
    content = models.TextField()
    image   = models.ImageField(upload_to='article_img',blank=True,null=True)
    
    published = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title