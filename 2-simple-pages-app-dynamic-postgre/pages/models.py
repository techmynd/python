from django.db import models

# Create your models here.

# class with single name of record type
# for pages > class would be page with uppercase first letter


class Page(models.Model):
    title = models.CharField(max_length=200)
    details = models.TextField()
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
