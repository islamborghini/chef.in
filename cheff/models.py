from django.db import models

# Categories of recipes
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'  # Correct pluralization for admin interface


# All of the recipes
class Recipies(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=1000, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product')
    ingredients = models.TextField(default='', blank=True, null=True)  # Multiline field for ingredients
    instructions = models.TextField(default='', blank=True, null=True)  # Multiline field for instructions

    def get_ingredients_list(self):
        # Split ingredients by lines and strip whitespace
        return [ingredient.strip() for ingredient in self.ingredients.splitlines() if ingredient.strip()]

    def get_instructions_list(self):
        # Split instructions by lines and strip whitespace
        return [step.strip() for step in self.instructions.splitlines() if step.strip()]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'recipies'  # Correct pluralization for admin interface

class Ratings(models.Model):
    name = models.ForeignKey(Recipies,on_delete=models.CASCADE )
    rating  = models.FloatField(max_length=1)

