# virtualStore/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from usuarios.views import index
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('usuarios.urls')),
    path('', index),    
    path('usuarios/', include('usuarios.urls')),
    
]
