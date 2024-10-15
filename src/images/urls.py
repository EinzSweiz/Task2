from django.urls import path
from . import views

app_name = 'images'

urlpatterns = [
    path('', views.create_image_view, name='image_create')
]