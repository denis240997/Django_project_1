from django.shortcuts import render
from django.views import View
from django.http import Http404

from tours import data


class MainView(View):
    def get(self, request):
        if False:
            raise Http404
        return render(request, 'tours/index.html')


class DepartureView(View):
    def get(self, request, departure):
        if False:
            raise Http404
        return render(request, 'tours/departure.html')


class TourView(View):
    def get(self, request, id):
        if False:
            raise Http404
        return render(request, 'tours/tour.html')
