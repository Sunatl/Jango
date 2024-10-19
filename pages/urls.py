from django.urls import path
from .views import home,say_hello,main,main1

urlpatterns = [
    path("Html", home),
    path("CSS",say_hello),
    path("Flag",main),
    path("Shakhmat",main1)
]