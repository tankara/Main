from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('hizmetlerimiz', views.services),
    path('hakkimizda', views.about),
    path('iletisim', views.contact),
    path('sss', views.sss),

    

]
