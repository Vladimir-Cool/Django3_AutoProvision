from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('content', views.content, name='content'),
    path('admin/', admin.site.urls),
    path('gateway/', include('voicegateway.urls')),
    ]
