from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('subjects/', views.subjects_view, name='subjects'),
    path('result/', views.result_view, name='result'),
    path('save-elective/', views.save_elective, name='save_elective'),
]