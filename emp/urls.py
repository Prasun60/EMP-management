from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path("home/",emphome),
    path("add-emp/",addemp),
    path("delete-emp/<int:empid>",deleteemp),
    path("update-emp/<int:empid>",updateemp),
    path("do-update-emp/<int:emp_id>",do_update_emp),
    path("testimonials/",testimonials),
]