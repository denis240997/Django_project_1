from django.views.generic.base import TemplateView
from django.http import Http404

import random
import tours.data as data


class BaseView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = data.title
        context['departures'] = data.departures
        return context


class MainView(BaseView):

    template_name = 'tours/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subtitle'] = data.subtitle
        context['description'] = data.description
        context['tour_random_list'] = random.sample(data.tours.items(), 6)
        return context


class DepartureView(BaseView):

    template_name = 'tours/departure.html'

    def get_context_data(self, departure, **kwargs):

        def filter_by_dep(tour):
            return tour[1]['departure'] == departure

        def price_filter_func(tour):
            return tour[1]['price']

        def nights_filter_func(tour):
            return tour[1]['nights']

        context = super().get_context_data(**kwargs)
        try:
            context['departure'] = data.departures[departure]
        except KeyError:
            raise Http404
        tour_departure_list = list(filter(filter_by_dep, data.tours.items()))
        context['tour_departure_list'] = tour_departure_list
        context['price_range'] = [min(tour_departure_list, key=price_filter_func)[1]['price'],
                                  max(tour_departure_list, key=price_filter_func)[1]['price']]
        context['nights_range'] = [min(tour_departure_list, key=nights_filter_func)[1]['nights'],
                                   max(tour_departure_list, key=nights_filter_func)[1]['nights']]
        return context


class TourView(BaseView):

    template_name = 'tours/tour.html'

    def get_context_data(self, id, **kwargs):
        context = super().get_context_data(**kwargs)
        for key, value in data.tours[id].items():
            context[key] = value
        context['stars'] = range(int(context['stars']))
        context['departure'] = data.departures[context['departure']]
        return context
