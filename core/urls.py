from django.contrib import admin
from django.urls import path, include

# Creating a route for the API's URLS
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
