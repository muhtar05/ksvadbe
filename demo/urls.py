from django.conf.urls import patterns,url
from demo import views

urlpatterns = patterns('demo.views',
   url(r'^$',views.DemoHomeView.as_view()),
   # url(r'^$',views.PhotoListView.as_view()),
   url(r'^test/$',views.TestView.as_view()),
   url(r'^users/$',views.UsersListView.as_view()),
   url(r'^testusers/$',views.TestUserView.as_view(),name='test_users'),
)
