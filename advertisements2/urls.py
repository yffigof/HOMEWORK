from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lesson_4', include('app_lesson_4.urls')),
    # path('', include('app_advertisements.urls')),
]

