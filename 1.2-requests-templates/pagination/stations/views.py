from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.conf import settings
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open(settings.BUS_STATION_CSV, 'r', encoding='UTF-8') as file:
        content = list(csv.reader(file, delimiter=','))
    data = []
    for line in content[1:]:
        data.append({'Name': line[1], 'Street': line[4], 'District': line[6]})

    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(data, 10)
    page = paginator.get_page(page_number)
    context = {
        'page': page,
        'bus_stations': page
    }
    return render(request, 'stations/index.html', context)
