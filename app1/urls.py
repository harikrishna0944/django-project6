from django.urls import path,include
from app1.views import *
app_name="somting"

urlpatterns = [
    path("first/",first,name="first"),
    
]
