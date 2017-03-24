#dojo/urls.py
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^sum/(?P<x>\d+)/$', views.mysum),
    #뒤에 $가 없을시 이 인자만 출력
    url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/$', views.mysum),
    url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/(?P<z>\d+)/$', views.mysum),
]
