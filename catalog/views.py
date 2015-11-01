# -*- coding: utf-8 -*- from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404,render_to_response,redirect
from django.views.generic import ListView, DetailView, View
from django.views.generic.detail import SingleObjectMixin
from catalog.models import Category, Firm,Product
from twython import Twython, TwythonError
from django.http import HttpResponseRedirect,HttpResponse
from cart import Cart
import pprint


def add_to_cart(request,product_id,quantity):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.add(product,product.price,quantity)
    return redirect('/cart/')

def get_cart(request):
    return render_to_response('catalog/cart.html',dict(cart=Cart(request)))


class TwitterView(View):
    def get(self, request, *args, **kwargs):
        APP_KEY = 'Yf8q3TPgL59StYj8KRlsAMmLu'
        APP_SECRET = 'KuMfl4Kvu0Y5W8qVYbusiu6L5x78wK3jpDJV1WAPfcjEy6zAvA'
        OAUTH_TOKEN = "198514629-mTKORfs9NmA29kfbnxrU9bCzyc8NvrzFDP9XLiTw"
        OAUTH_TOKEN_SECRET = 'r9u7SJPrc7u7Vy9pz66uMrfcBSzL8he6HRHprJgEC6bGQ'
        twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        try:
            search_term = request.GET.get('srch-term', 'twitter')
            search_results = twitter.search(q=search_term, count=10)
        except TwythonError as e:
            print e


        my_updates = twitter.get_friends_list(count=500)
        my_updates = my_updates['users']
        the_type = type(my_updates)


        return render(request, "catalog/twitter.html", {
            'search_results': search_results['statuses'],
            'my_updates': my_updates,
            'the_type': the_type
        })


class CategoryListView(ListView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['firms_list'] = Firm.objects.all()[:9]
        return context


class FirmListView(ListView):
    model = Firm


class FirmDetailView(DetailView):
    model = Firm


    def get(self,request,**kwargs):
        self.object = Firm.objects.get(alt_title=self.kwargs['alt_title'])
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(FirmDetailView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request,**kwargs):
        self.object = Category.objects.get(alt_name =self.kwargs['alt_name'])
        if self.request.path != self.object.get_absolute_url():
            return HttpResponseRedirect(self.object.get_absolute_url())
        else:
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)


    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context

class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView,self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context


