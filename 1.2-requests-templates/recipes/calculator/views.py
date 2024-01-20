from django.http import HttpResponse
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
    'butter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
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
def omlet(request):
    serving = int(request.GET.get('serving', 1))
    for ing in DATA['omlet']:
        DATA['omlet'][ing] = DATA['omlet'][ing] * serving
    context = {
        'recipe': DATA['omlet']
    }
    return render(request, 'calculator/index.html', context)


def pasta(request):
    serving = int(request.GET.get('serving', 1))
    for ing in DATA['pasta']:
        DATA['pasta'][ing] = DATA['pasta'][ing] * serving
    context = {
        'recipe': DATA['pasta']
    }
    return render(request, 'calculator/index.html', context)


def butter(request):
    serving = int(request.GET.get('serving', 1))
    for ing in DATA['butter']:
        DATA['butter'][ing] = DATA['butter'][ing] * serving
    context = {
        'recipe': DATA['butter']
    }
    return render(request, 'calculator/index.html', context)
