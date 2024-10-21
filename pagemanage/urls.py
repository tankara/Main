from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('hizmetlerimiz', views.services, name="hizmetlerimiz"),
    path('hakkimizda', views.about, name="hakkimizda"),
    path('iletisim', views.contact),
    path('ogretmenler', views.teachers, name="teachers"),
    path('sss', views.sss),
]
