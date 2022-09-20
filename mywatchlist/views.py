from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

def show_mywatchlist(request):
    data_film_mywatchlist = MyWatchList.objects.all()
    context = {
    'list_film': data_film_mywatchlist,
    'nama': 'Muhammad Arief Braja Putra',
    'npm': '2106702352'
}
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

