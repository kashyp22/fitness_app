"""AI_based_fitness_application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from myapp import views
#
# urlpatterns = [
#     path('logins/', views.logins),
#     path('login_get/', views.login_get),
#     path('admin_home/',views.admin_home),
#     path('add_service_plan/',views.add_service_plan),
#     path('add_trainer/',views.add_trainer),
#     path('add_video/',views.add_video),
#     path('assign_trainers/',views.assign_trainers),
#     path('change_password/',views.change_password),
#     path('send_reply/',views.send_reply),
#     path('view_assigned_trainer/<id>',views.view_assigned_trainer),
#     path('view_complaint/',views.view_complaint),
#     path('view_review/',views.view_review),
#     path('view_trainer/',views.view_trainer),
#     path('view_service_plans/',views.view_service_plans),
#     path('view_workout_plan/',views.view_workout_plan),
#     path('view_workout_video/',views.view_workout_video),
#     path('add_service_plan_post/',views.add_service_plan_post),
#     path('add_trainer_post/', views.add_trainer_post),
#     path('add_video_post/', views.add_video_post),
#     path('assign_trainer_post/', views.assign_trainer_post),
#     path('change_password_post/', views.change_password_post),
#     path('send_reply_post/', views.send_reply_post),
#     path('add_entiquette_post/', views.add_entiquette_post),
#     path('add_entiquette/', views.add_entiquette),
#     path('view_entiquette/', views.view_entiquette),
#     path('edit_service_plan/<id>', views.edit_service_plan),
#     path('edit_service_plan_post/', views.edit_service_plan_post),
#     path('delete_service_plan/<id>', views.delete_service_plan),
#     path('delete_workout_video/<id>', views.delete_workout_video),
#     path('edit_trainer/<id>', views.edit_trainer),
#     path('edit_trainer_post/', views.edit_trainer_post),
#     path('delete_trainer/<id>', views.delete_trainer),
#     path('delete_entiquette/<id>', views.delete_entiquette),
#     path('edit_entiquette/<id>',views.edit_entiquette),
#     path('edit_entiquette_post/',views.edit_entiquette_post),
#     path('edit_entiquette_post/',views.edit_entiquette_post),
#     path('logout/',views.logout),
#
# ]

################tainner##################
from django.urls import path
from . import views


urlpatterns = [

    path('logins/', views.logins),
    path('login_get/', views.login_get),
    path('admin_home/',views.admin_home),
    path('add_service_plan/',views.add_service_plan),
    path('add_trainer/',views.add_trainer),
    path('add_video/',views.add_video),
    path('assign_trainers/',views.assign_trainers),
    path('change_password/',views.change_password),
    path('send_reply/',views.send_reply),
    path('view_assigned_trainer/<id>',views.view_assigned_trainer),
    path('view_complaint/',views.view_complaint),
    path('view_review/',views.view_review),
    path('view_user/',views.view_user),
    path('view_trainer/',views.view_trainer),
    path('view_service_plans/',views.view_service_plans),
    path('view_workout_plan/',views.view_workout_plan),
    path('view_workout_video/',views.view_workout_video),
    path('add_service_plan_post/',views.add_service_plan_post),
    path('add_trainer_post/', views.add_trainer_post),
    path('add_video_post/', views.add_video_post),
    path('assign_trainer_post/', views.assign_trainer_post),
    path('change_password_post/', views.change_password_post),
    path('send_reply_post/', views.send_reply_post),
    path('add_entiquette_post/', views.add_entiquette_post),
    path('add_entiquette/', views.add_entiquette),
    path('view_entiquette/', views.view_entiquette),
    path('edit_service_plan/<id>', views.edit_service_plan),
    path('edit_service_plan_post/', views.edit_service_plan_post),
    path('delete_service_plan/<id>', views.delete_service_plan),
    path('delete_workout_video/<id>', views.delete_workout_video),
    path('edit_trainer/<id>', views.edit_trainer),
    path('edit_trainer_post/', views.edit_trainer_post),
    path('delete_trainer/<id>', views.delete_trainer),
    path('delete_entiquette/<id>', views.delete_entiquette),
    path('edit_entiquette/<id>',views.edit_entiquette),
    path('edit_entiquette_post/',views.edit_entiquette_post),
    path('edit_entiquette_post/',views.edit_entiquette_post),
    path('logout/',views.logout),



    path("trainerindex/",views.trainerindex),
    # path('login/',views.trainer_login_index,name='trainer_login_index'),
    path('add_diet_plan/',views.add_diet_plan),
    path('add_diet_plan_post/',views.add_diet_plan_post),
    path('add_motivational_video/',views.add_motivational_video),
    path('delete_video/<id>', views.delete_video),

    path('add_motivational_video_post/',views.add_motivational_video_post),
    path('add_tips/',views.add_tips),
    path('add_tips_post/',views.add_tips_post),
    path('delete_tips/<id>', views.delete_tips),
    path('add_workoutplan/',views.add_workoutplan),
    path('add_workoutplan_post/',views.add_workoutplan_post),
    path('change_password/',views.change_password),
    path('change_password_POST/',views.change_password_POST),
    path('edit_diet_plan/',views.edit_diet_plan),
    path('edit_diet_plan_POST/',views.edit_diet_plan_POST),
    path('edit_tips/<id>',views.edit_tips),
    path('edit_tips_post/',views.edit_tips_post),
    path('view_accepted_request/',views.view_accepted_request),
    path('view_assign/',views.view_assign),
    path('view_diet_plan/',views.view_diet_plan),
    path('view_fee_alert/',views.view_fee_alert),
    path('view_gym_entiquette/',views.view_gym_entiquette),
    path('view_motivatioal_video/',views.view_motivatioal_video),
    path('view_profile/',views.view_profile),
    path('view_serviceplan/',views.view_serviceplan),
    path('user_request_approve/<id>',views.user_request_approve),
    path('user_request_reject/<id>',views.user_request_reject),

    path('view_user_service_request/<id>',views.view_user_service_request),
    path('view_tips/',views.view_tips),
    path('view_user_request/',views.view_user_request),
    path('view_user_serviceplan/',views.view_user_serviceplan),
    path('view_workoutplan/',views.view_workoutplan),
    path('user_view_trainers/',views.user_view_trainers),
    path('user_view_service/',views.user_view_service),
    path('user_view_workout_plans/',views.user_view_workout_plans),
    path('user_view_diet_plan/',views.user_view_diet_plan),
    path('user_view_tip/',views.user_view_tip),
    path('user_view_workout_video/',views.user_view_workout_video),
    path('user_view_motivated_video/',views.user_view_motivated_video),


    # ===============user==============

    path('flutter_login/',views.flutter_login),
    path('UserRegistration/',views.UserRegistration),
    path('request_trainer/',views.request_trainer),
    path('view_request_status/',views.view_request_status),





    ]