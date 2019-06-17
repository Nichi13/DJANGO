from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from urllib.parse import urlencode
import csv
from django.conf import settings


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    get_page = request.GET.get('page')
    set_path = settings.BUS_STATION_CSV
    bus_stations_info = []
    with open(set_path, encoding='cp1251', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for item in reader:
            bus_station_info = {'Name': item['Name'], 'Street': item['Street'], 'District': item['District']}
            bus_stations_info.append(bus_station_info)
    if get_page is None:
        page = 1
        page_down = None
    elif int(get_page) == 1:
        page = 1
        page_down = None
    else:
        page = int(get_page)
        page_down = '?' + urlencode({'page': page - 1})
    page_up = '?' + urlencode({'page': page+1})
    return render_to_response('index.html', context={
        'bus_stations': bus_stations_info[(page - 1)*10:page*10],
        'current_page': page,
        'prev_page_url': page_down,
        'next_page_url': page_up})