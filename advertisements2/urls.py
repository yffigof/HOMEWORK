from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('app_lesson_4.urls')),
    path('admin/', admin.site.urls),
# path('', include('app_advertisements.urls')),
]

