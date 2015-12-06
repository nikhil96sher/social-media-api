from django.conf.urls import patterns,url
from hashtag import views

urlpatterns=patterns(
'',
url(r'^result/$',views.findstory),
url(r'^home/$',views.home),
)
