
from django.contrib import admin
from .views import main
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main)
]