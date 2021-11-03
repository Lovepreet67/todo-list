from django.urls import path
from . import views

urlpatterns = [
    path("home",views.index , name = "index"),
    path("signup" ,views.signup, name = "signup"),
    path("" ,views.loginx ,name = "loginx"),
    path("add", views.add , name = "add"),
    path("remove",views.remove , name = "remove"),
    path("about" ,views.about , name = "about"),
    path("logout" , views.logoutx , name = 'logout')
]
