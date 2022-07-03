from django import template
from django.utils import timezone


register = template.Library()


@register.filter
def division(num1, num2):
    return int(num1 // num2)

@register.filter
def mul_(num1, num2):
    return int((int(num1 * num2)) / 1000)*1000
    

@register.filter
def mul_100(num1):
    return int(100-num1*100)