from django.shortcuts import render
from .models import GrapeVarity, WineVarity, StoredBarrel


def get_all_grapes():
    "Получает все сорта винограда из базы данных"
    return GrapeVarity.objects.all()


def get_all_wines():
    "Получает все сорта вин из базы данных"
    return WineVarity.objects.all()


def get_all_storeds():
    "Получает информацию обо всех бочках из базы данных"
    return StoredBarrel.objects.all()


def index(request):

    data = {
        'grapes': get_all_grapes(),
        'wines': get_all_wines(),
        'storeds': get_all_storeds(),
    }

    return render(request, 'home/index.html', data)

