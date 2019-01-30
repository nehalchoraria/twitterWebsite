from django.urls import path
from .views import homePage,tweetdetails
from django.conf.urls import url

urlpatterns = [
    path('tweet/<int:id>',tweetdetails),
    path('',homePage),
    # path('',homePage),
]
