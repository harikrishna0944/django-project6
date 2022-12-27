from django.urls import path,include
from app2.views import *
app_name="somting1"

urlpatterns = [
    path("second/",second,name="second"),
    
]
