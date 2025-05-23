

from django.urls import path

from jobhub import views


urlpatterns = [
    path("user_registration_get/",views.user_registration_get,name="user_registration_get"),
    path("user_registration_post/",views.user_registration_post,name="user_registration_post"),
    path("login_get/",views.login_get,name="login_get"),
    path("login_post/",views.login_post,name="login_post"),

]
