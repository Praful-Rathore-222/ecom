from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=40)

    # def get_all_categories():
    #     Category.objects.all()
    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=40)
    price=models.IntegerField(default=0)
    description=models.CharField(max_length=200, default='')
    category=models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    image=models.ImageField(upload_to="images/")