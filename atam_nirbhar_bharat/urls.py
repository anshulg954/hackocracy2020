from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('HomeIndex.urls')),
    path('startUP/', include('start_app.urls')),
    path('jobify/', include('first_look.urls')), 
]
