from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from ksvadbe05.views import HomeView,test,success,login,maps
from catalog.models import Firm,Category,Product
from catalog.views import ProductDetailView,get_cart,add_to_cart
from django.contrib.sitemaps import GenericSitemap

admin.autodiscover()

info_dict = {
    'queryset':Firm.objects.all()
}

info_dict_category = {
    'queryset':Category.objects.all()
}

info_dict_product = {
    'queryset':Product.objects.all()
}

sitemaps = {
    'category': GenericSitemap(info_dict_category,priority=0.6),
    'firm': GenericSitemap(info_dict,priority=0.6,),
    'product': GenericSitemap(info_dict_product,priority=0.9,)
}

urlpatterns = patterns('',
    # Examples:
     url(r'^$', HomeView.as_view(), name='home'),
     url(r'^test/$', test, name='test'),
     url(r'^maps/$',maps, name='maps'),
     url(r'^login/$',login, name='login'),
     url(r'^logged-in/$',success, name='success'),
     url(r'^cart/$',get_cart),
     url(r'^cart/add/(?P<product_id>[0-9]+)/(?P<quantity>[0-9]+)/$',add_to_cart),
     url(r'^product/(?P<pk>[0-9]+)/$',ProductDetailView.as_view()),
     url(r'^catalog/', include('catalog.urls')),
     url(r'^demo/', include('demo.urls')),
     url(r'^posts/', include('posts.urls')),
     url(r'', include('social_auth.urls')),

     url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
     url(r'^admin/', include(admin.site.urls)),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
