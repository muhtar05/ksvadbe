from django.conf.urls import patterns,url
from catalog import views

urlpatterns = patterns('catalog.views',
   url(r'^$',views.CategoryListView.as_view()),
   url(r'^twitter$',views.TwitterView.as_view()),
   url(r'^(?P<alt_name>[-\w]+)$',views.CategoryDetailView.as_view(),name='category-detail'),
   url(r'^firms$',views.FirmListView.as_view()),
   url(r'^firm/(?P<alt_title>[-\w]+).html$',views.FirmDetailView.as_view(),name='firm-detail'),
)
