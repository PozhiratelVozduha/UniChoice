from django.urls import path
from . import views 

urlpatterns = [
    path('', views.base, name='base'),
    path("tech/", views.tech_universities, name="tech_universities"),
    path("med/", views.med_universities, name="med_universities"),
    path("human/", views.human_universities, name="human_universities"),
    path("art/", views.art_universities, name="art_universities"),
]