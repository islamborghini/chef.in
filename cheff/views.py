from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipies, Ratings
from django.db.models import Avg
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .edamam_client import EdamamClient
from .models import Category
from django.db.models import Q
import logging

def home(request):
    # Retrieve all recipes and render the home page
    recipies = Recipies.objects.all()
    return render(request, 'home.html', {'recipies': recipies})


def recipy_detail(request, pk):
    # Retrieve the recipe by primary key or return a 404 if not found
    recipy = get_object_or_404(Recipies, pk=pk)
    edamam_client = EdamamClient()
    title = recipy.name
    ingredients = recipy.get_ingredients_list()
    ratings = Ratings.objects.filter(name=recipy)
        
    # Analyze the recipe using the Edamam API
    analysis_result = edamam_client.analyze_recipe(title, ingredients)
    
    return render(request, 'recipy.html', {
        'recipies': recipy,
        'ingredients': recipy.get_ingredients_list(),
        'instructions': recipy.get_instructions_list(),
        'analysis': analysis_result,
        'ratings': ratings
    })

def search(request):
    # Check if the search form was submitted
    if request.method == "POST":
        searched = request.POST['searched']
        # Filter recipes based on search query in name or description
        searched = Recipies.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched))

        # Check if any recipes were found
        if not searched: 
            messages.error(request, "That product does not exist, please try again")
            return render(request, 'search.html', {})
        else:
            return render(request, 'search.html', {'searched': searched})
    else:
        return render(request, 'search.html', {})

def category(request, ggg):
    try:
        # Lookup the category by name
        category = Category.objects.get(name=ggg)
        recipies = Recipies.objects.filter(category=category)
        return render(request, 'category.html', {'recipies': recipies, 'category': category})
    except ObjectDoesNotExist:
        # Handle case where the category does not exist
        messages.error(request, "That category doesn't exist")
        logging.error(f"Category '{ggg}' does not exist.")
        return redirect('home')

def about(request):
    # Render the about page
    return render(request, 'about.html', {})

def recipy(request, pk):
    # Retrieve a single recipe by primary key
    recipies = Recipies.objects.get(id=pk)
    return render(request, 'recipy.html', {'recipies': recipies})
