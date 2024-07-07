from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },

}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

# def convert_data_to_context(data):
#     recipes = []
#     for recipe_name, ingredients in data.items():
#         recipe = {recipe_name: {}}
#         for ingredient, quantity in ingredients.items():
#             ingredient_key = f"{ingredient.split(',')[0].strip()}"
#             recipe[recipe_name][ingredient_key] = quantity
#         recipes.append(recipe)
#     return recipes

# context = convert_data_to_context(DATA)

def recipe_view(request, recipe_name):
    servings = int(request.GET.get('servings', 1))
    recipe_data = DATA.get(recipe_name)
    if recipe_data:
        context = {
            'recipe': {k: v * servings for k, v in recipe_data.items()}
        }
        return render(request, 'calculator/index.html', context)
    else:
        return render(request, 'calculator/404.html', {'error_message': f"Recipe '{recipe_name}' not found"},
                      status=404)

   


    