from django.shortcuts import render

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
    # можете добавить свои рецепты ;)
}


def recipe_view(request, recipe_name):
    """
    Обработчик для отображения рецепта.
    Поддерживает опциональный параметр servings для масштабирования порций.
    """
    # Получаем рецепт из DATA
    recipe_data = DATA.get(recipe_name, {})
    
    # Получаем количество порций из GET-параметров (по умолчанию 1)
    servings = 1
    if 'servings' in request.GET:
        try:
            servings = int(request.GET.get('servings'))
            if servings < 1:
                servings = 1
        except (ValueError, TypeError):
            servings = 1
    
    # Масштабируем количество ингредиентов на количество порций
    scaled_recipe = {
        ingredient: amount * servings
        for ingredient, amount in recipe_data.items()
    }
    
    context = {
        'recipe': scaled_recipe
    }
    
    return render(request, 'calculator/index.html', context)
