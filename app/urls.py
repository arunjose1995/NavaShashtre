from django.urls import path, re_path
from app import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('edit-profile/', views.edit_profile, name='edit-profile'),
    path('profile/', views.save_profile, name='save-profile'),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
