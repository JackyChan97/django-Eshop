from django.db import models
from login.models import User
# Create your models here.
class Goods(models.Model):

    category = (
        ("MW","Men's wear"),
        ("WW","Women's wear"),
        ("CW","Children's wear"),
    )
    name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    userName = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_goods", blank=True, null=True)
    introduction = models.CharField(max_length=1024)
    imagePath = models.ImageField(upload_to="upload/%y/%m/%d",default='', blank=True)
    kind = models.CharField(max_length=32,choices=category,default="Men's wear")
    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "商品"
        verbose_name_plural = "商品"

