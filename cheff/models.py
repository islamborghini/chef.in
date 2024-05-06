from django.db import models


# Categories of recipies
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'

# All of the recipies
# models.py

class Recipies(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=1000, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product')
    ingredients = models.TextField(default='', blank=True, null=True)  # Multiline TextField for ingredients
    instructions = models.TextField(default='', blank=True, null=True)  # Multiline TextField for instructions

    def get_ingredients_list(self):
        return [ingredient.strip() for ingredient in self.ingredients.splitlines() if ingredient.strip()]

    def get_instructions_list(self):
        return [step.strip() for step in self.instructions.splitlines() if step.strip()]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'recipies'

