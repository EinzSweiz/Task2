from django.urls import path
from . import views

app_name = 'images'

urlpatterns = [
    path('', views.create_image_view, name='image_create'),
    path('images/', views.image_list_view, name='image_list'),
    path('download/', views.image_download_view, name='image_download'),

]