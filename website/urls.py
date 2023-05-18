from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("animao.urls")),
    path("admin/", admin.site.urls),
]