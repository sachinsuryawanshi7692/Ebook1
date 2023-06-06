from django.db import models

# Create your models here.

class Product(models.Model):
    CAT=((1,'Historical'),(2,'Biography'),(3,'Cook'),(4,'Poetry'))
    name=models.CharField(max_length=60,verbose_name="Book Name")
    cat=models.IntegerField(verbose_name="Category",choices=CAT)
    price=models.FloatField(verbose_name="Book Price")
    date=models.DateField()
    status=models.BooleanField(default=True)
    eimage=models.ImageField(upload_to="Image")


    def __str__(self):
        return self.name
