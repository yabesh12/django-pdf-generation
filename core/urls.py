from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name="home"),
    path('download/', views.convert_to_pdf, name="download"),
]
