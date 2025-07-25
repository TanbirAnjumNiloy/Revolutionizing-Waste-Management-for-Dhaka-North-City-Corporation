from django.contrib import admin
from django.urls import path
from role import views
from django.urls import path

from django.views.generic import TemplateView
from django.urls import path


from django.contrib import admin
from django.urls import path
from role import views
from .views import new_login_view


from .views import new_login_view , allusers ,createuser,Getuser

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),

    path("dashboard/", views.dashboard, name="dashboard"),
    path("adminprofile/", views.adminprofile, name="adminprofile"),


    path("logout/", views.logout_view, name="logout"),
    path("change-password/", views.change_password_view, name="change_password"),
    path("create/new/user/", views.create_new_user, name="create_new_user"),
    path("user", views.see_all_user, name="see_all_users"),
    path("roles", views.see_all_role, name="see_all_role"),
    path("deleteuser", views.datale_user, name="datale_user"),
    path("updateusername", views.update_user_name, name="update_user_name"),
    path("profile/update/", views.user_profile_update, name="user_profile_update"),
    path("rbac/roles", views.change_user_roll, name="change_user_roll"),
    path("stsmanager/profile", views.sts_manager, name="sts_manager"),
    path("landfillmanager/profile", views.landfill_manager, name="landfill_manager"),
    path("unassigned/profile", views.unassigned, name="unassigned"),
    path("new-login/", new_login_view, name="new_login"),
    path("vehicle/create/", views.vehicle_create, name="vehicle_create"),
    path("vehiclesuccess", views.vehiclesuccess, name="vehiclesuccess"),
    path("success", views.success, name="success"),
    path("sts/create", views.sts_create, name="sts_create"),
    path("landfill/create", views.landfill_create, name="landfill_create"),

    path('control/users/persimmon/', views.control_users_persimmon, name='Control_Users_Persimmon'),



    path('calculate_cost/', views.calculate_cost, name='calculate_cost'),
    path('generate_pdf/<int:vehicle_id>/', views.generate_pdf, name='generate_pdf'),

    



    path("sts_manager/create", views.sts_manager_create, name="sts_manager_create"),
    path(
        "landfill_manager_create/",
        views.landfill_manager_create,
        name="landfill_manager_create",
    ),
    path("sts_entry/create/", views.create_sts_entry, name="create_sts_entry"),
    path(
        "landfill_entry/create/",
        views.create_landfill_entry,
        name="create_landfill_entry",
    ),


    path("users", allusers.as_view(), name="see_all_user"),

    path("create/user", createuser.as_view(), name="createuser"),

    path("users/<int:pk>", Getuser.as_view(), name="getuser"),




    


    


]
