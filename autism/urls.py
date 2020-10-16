from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('predict', views.predict, name="predict"),
    path('predicted', views.predicted, name="predicted"),
    path('restapi/', views.restapi, name='restapi'),
    
]

#  http://127.0.0.1:8000/restapi/?value1=1&value2=1&value3=1&value4=1&value5=1&value6=1&value7=1&value8=1