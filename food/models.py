from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

def upload_food_img(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.en_name, ext)
    return '/'.join(['foods', instance.en_name, filename])


class Food(models.Model):
    name = models.CharField(max_length=100)
    en_name = models.CharField(max_length=100)
    price = models.IntegerField()
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to=upload_food_img)
    description = models.TextField(null=True)


class DiscountFood(models.Model):
    time = models.DateTimeField(default=timezone.now)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_creat_discount', null=True, blank=True)
    value = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(1)])
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()