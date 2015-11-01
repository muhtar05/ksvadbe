from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from catalog.models import Firm,Product
from pprint import pprint
from social_auth.models import UserSocialAuth



class HomeView(View):

    def get(self,request,*args,**kwargs):
        firms = Firm.objects.all().order_by('?')[:12]
        last_product = Product.objects.all()[:6]
        user_info = request.user
        return render(request,"ksvadbe05/home.html",{
            "firms":firms,
            "last_product":last_product,
            'user_info':user_info
        })


def maps(request):
    return render(request,'ksvadbe05/maps.html')

def test(request):
    instance = UserSocialAuth.objects.filter(provider='facebook')
    out = pprint(instance.token)
    return HttpResponse(out)


def success(request):
    user=request.user
    return HttpResponse("Hello my friend %s" %user)


def login(request):
    users = UserSocialAuth.objects.all()
    return render(request,'ksvadbe05/login.html',{
        'users':users
    })

