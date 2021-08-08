from django.urls import path, re_path
from app import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    # Profile page
    path('edit-profile/', views.edit_profile, name='edit-profile'),
    path('profile/', views.save_profile, name='save-profile'),
    # Laptop page
    path('view-asset/', views.view_asset, name='view-asset'),
    path('add-asset/', views.add_asset, name='add-asset'),
    path('save-asset/', views.save_asset, name='save-asset'),
    path('edit-asset/<int:asset_id>', views.edit_asset, name='edit-asset'),
    path('update-asset/<int:asset_id>', views.update_asset, name='update-asset'),
    path('delete-asset/<int:asset_id>', views.delete_asset, name='delete-asset'),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
