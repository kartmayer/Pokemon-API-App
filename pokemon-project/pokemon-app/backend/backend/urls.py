from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/pokedex/', include('pokedex.urls')),
    path('api/users/', include('users.urls')),
]