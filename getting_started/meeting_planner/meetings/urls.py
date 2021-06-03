from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>', views.details, name='detail'),
    path("rooms", views.rooms_details, name='room_details'),
    path("new", views.new, name='new')
]