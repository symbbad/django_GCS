from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "app"

urlpatterns = [
    path("", views.main, name="main"),
    path("testcase_1/", views.testcase_1, name="testcase_1"),
    path("write/", views.write, name="write")
]
