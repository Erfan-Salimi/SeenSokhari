from django.shortcuts import render, redirect
from food.models import *
from django.utils import timezone
from datetime import datetime

# Create your views here.

def home(request):
    foods = Food.objects.filter(available=True)
    discounts = DiscountFood.objects.filter(start_time__lte=datetime.now()).filter(end_time__gte=datetime.now()).order_by("-time")
    price = 100
    for i in discounts:
        price = price - ((i.value / 100) * price)
    return render(request, 'Home.html', context={'foods': foods, 'discount': price*0.01})
