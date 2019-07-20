
from django.conf.urls import url
from . import views

urlpatterns = [
   
    # url('contact',views.contact),
    url('count',views.count, name='count'),
    url('about',views.about, name='about'),
    url('',views.homepage, name= 'home'),
]
