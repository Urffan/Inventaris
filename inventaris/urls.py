from django.contrib import admin
from django.urls import path

from master import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/',views.index, name='list'),
]