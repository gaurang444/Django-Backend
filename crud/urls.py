
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
import crud.views as views

user_urlpatterns = [
    url(r'^home/$',views.home_view, name='all-users'),
    url(r'^add/$',views.add_user, name='user-create'),
    url(r'^update/$',views.update_user, name='user-update'),
    url(r'^delete/$',views.delete_user, name='user-delete'),
    
]