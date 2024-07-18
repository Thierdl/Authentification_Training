
from django.contrib import admin
from django.urls import include, path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_views, name='index'),
    path('login/', include('authentification.urls')),
    
]
