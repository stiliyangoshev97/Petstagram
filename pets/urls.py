from django.urls import path
from pets import views

app_name = 'pets'

urlpatterns = [
    path('create_pet/', views.create_pet, name='create_pet'),
    path('edit_pet/<pk>', views.edit_pet, name='edit_pet'),
    path('remove_pet/<pk>', views.remove_pet, name='remove_pet'),
    path('pets_list/', views.pets_list, name='pets_list'),
    path('pet_details/<pk>', views.pet_details, name='pet_details'),
    path('pet_like_pet/<pk>', views.like_pet, name='like_pet'),
    path('pet_dislike_pet/<pk>', views.dislike_pet, name='dislike_pet'),


]