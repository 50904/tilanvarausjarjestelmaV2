from django.urls import path
from . import views

urlpatterns = [
    # Main URL
    path('', views.main, name='main'),
    # Käyttäjät URLs
    path('user/', views.user, name='user'),
    path('user/users_details/<slug:slug>', views.users_details, name='users_details'),
    # Tilat URLs
    path('space/', views.space, name='space'),
    path('space/spaces_details/<slug:slug>', views.spaces_details, name='spaces_details'),
]