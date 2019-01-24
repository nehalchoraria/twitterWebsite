from django.urls import path
from .views import followers,followUnfollowUser

urlpatterns = [
    path('following/<str:name>',followUnfollowUser),
    path('following/<str:name>',followUnfollowUser),
    path('',followers),
]
