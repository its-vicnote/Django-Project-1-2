from django.urls import path
from . import views
urlpatterns = [ 
    path('', views.index),
    path('vic/', views.vic),
    path('vic2/', views.vic2)
]