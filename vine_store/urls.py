from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('vineApp.urls')),
    path('index/', include('vineApp.urls')),
    path('admin/', admin.site.urls),
]
