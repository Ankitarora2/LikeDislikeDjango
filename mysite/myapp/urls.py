from django.urls import path
from . import views

urlpatterns = [
    path('update-count/', views.update_count, name='update_count'),
]
