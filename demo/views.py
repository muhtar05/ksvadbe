import tweepy
import time
import requests

from django.views.generic import ListView, View ,TemplateView
from django.http import HttpResponse
from django.shortcuts import render
from demo.models import Photo
from catalog.models import Firm
from social_auth.models import UserSocialAuth

CONSUMER_KEY = 'Yf8q3TPgL59StYj8KRlsAMmLu'
CONSUMER_SECRET = 'KuMfl4Kvu0Y5W8qVYbusiu6L5x78wK3jpDJV1WAPfcjEy6zAvA'
ACCESS_KEY = '198514629-mTKORfs9NmA29kfbnxrU9bCzyc8NvrzFDP9XLiTw'
ACCESS_SECRET = 'r9u7SJPrc7u7Vy9pz66uMrfcBSzL8he6HRHprJgEC6bGQ'




class DemoHomeView(TemplateView):
    template_name = 'demo/demo_home.html'

    def get_context_data(self, **kwargs):
        firms  = Firm.objects.all()
        count_firms = Firm.objects.count()
        context = super(DemoHomeView,self).get_context_data(**kwargs)
        context['firms'] = firms
        context['count_firms'] = count_firms
        return context


class PhotoListView(ListView):
    model = Photo


class UsersListView(ListView):
    model = UserSocialAuth
    template_name = 'demo/users_list.html'


class TestView(TemplateView):

    template_name = 'demo/test.html'

    def get_context_data(self, **kwargs):
        context = super(TestView,self).get_context_data(**kwargs)
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        api = tweepy.API(auth)
        context['tweets'] = api.search(q='#mkala')
        context['current_user'] = api.get_user('muhtar05')
        return context



class TestUserView(TemplateView):

    template_name = 'demo/test_users.html'

    def get_context_data(self, **kwargs):
        context = super(TestUserView,self).get_context_data(**kwargs)
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        api = tweepy.API(auth)
        context['followers'] = api.followers()
        ids = []


        context['ids'] = ids
        return context