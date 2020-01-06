from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^info/', csrf_exempt(views.info), name='info'),
    url(r'^', views.index, name='index'),
]
