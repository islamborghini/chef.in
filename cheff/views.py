from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipies
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .edamam_client import EdamamClient
from .models import Category
from django.db.models import Q
import logging

def home(request):
    recipies = Recipies.objects.all()
    return render(request, 'home.html', {'recipies': recipies})


def recipy_detail(request, pk):
    recipy = get_object_or_404(Recipies, pk=pk)
    edamam_client = EdamamClient()
    title = recipy.name
    ingredients = recipy.get_ingredients_list()
    analysis_result = edamam_client.analyze_recipe(title, ingredients)
    
    return render(request, 'recipy.html', {
        'recipies': recipy,
        'ingredients': recipy.get_ingredients_list(),
        'instructions': recipy.get_instructions_list(),
        'analysis': analysis_result

    })


def search(request):
    #Determiner if they filled out the form
    if request.method =="POST":
        searched = request.POST['searched']
        searched = Recipies.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched) )

        #TEST FOR NULL
        if not searched: 
            messages.error(request, "That Product does not exist, please try again")
            return render(request, 'search.html', {})
        else:
            return render(request, 'search.html', {'searched': searched})

    else:
        return render(request, 'search.html', {})

def category(request, ggg):
    try:
        # Lookup the category
        category = Category.objects.get(name=ggg)
        recipies = Recipies.objects.filter(category=category)
        return render(request, 'category.html', {'recipies': recipies, 'category': category})
    except ObjectDoesNotExist:
        messages.error(request, "That category doesn't exist")
        logging.error(f"Category '{ggg}' does not exist.")
        return redirect('home')
def about(request):
	return render(request, 'about.html', {})

def recipy(request, pk):
	recipies = Recipies.objects.get(id=pk)
	return render(request,'recipy.html', {'recipies': recipies})