from django.shortcuts import render
from meals.models import Meals , Category
from blog.models import Post
from aboutus.models import Why_Choose_Us
# Create your views here.


def home(request):

    meals = Meals.objects.all()
    meal_list = Meals.objects.all()
    categories = Category.objects.all()
    why_choose_us = Why_Choose_Us.objects.all()


    
    context = {
        'meals' : meals ,
        'meal_list' : meal_list ,
        'categories' : categories ,
        'why_choose_us' : why_choose_us , 
    }

    return render(request , 'home/index.html' , context)