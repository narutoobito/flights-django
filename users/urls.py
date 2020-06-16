from django.urls import path

from . import views

app_name="users"

urlpatterns=[
    path("",views.index, name="index"),
    path("login/",views.lin, name="lin"),
    path("logout/<str:user>",views.lout,name="lout"),
]