from django.urls import include, path, re_path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url
from django.contrib.auth import views as forogotpassword_view


urlpatterns = [
    path('', home),
]
