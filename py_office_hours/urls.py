from django.contrib import admin
from django.urls import path
from attendess.views import current_time

urlpatterns = [
    path("admin/", admin.site.urls),
    path("time/", current_time),
]
