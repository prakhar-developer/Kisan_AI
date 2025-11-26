from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('select-language/', views.select_language, name='select_language'),
]
