from django.urls import path
from .views import homePage
from django.conf.urls import url

urlpatterns = [
    path('',homePage),
    # path('',homePage),
]
