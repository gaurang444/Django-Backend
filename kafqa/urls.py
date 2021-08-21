from django.contrib import admin
from django.urls import path
from crud.urls import user_urlpatterns
from django.conf.urls import url,include

urlpatterns = [
    url(r'^user/', include((user_urlpatterns, 'user-url-patterns'), namespace='user-urls')),
    url(r'^admin/',(admin.site.urls)),
]
