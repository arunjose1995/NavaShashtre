from django.urls import path
from .views import login_view, register_user, \
    get_users, add_user, \
    save_user, edit_user, \
    update_user, delete_user
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("users/", get_users, name="users"),
    path("add-user/", add_user, name="add-user"),
    path("save-user/", save_user, name="save-user"),
    path("edit-user/<int:user_id>", edit_user, name="edit-user"),
    path("update-user/<int:user_id>", update_user, name="update-user"),
    path("delete-user/<int:user_id>", delete_user, name="delete-user"),
]
