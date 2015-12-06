from django.conf.urls import patterns,include, url
from django.contrib import admin
from django.conf import settings
from hashtag import urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
	url(r'^hashtag/',include(urls)),
]