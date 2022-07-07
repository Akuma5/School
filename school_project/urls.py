# school_project URL
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', include('courses_app.urls')),
    path('students/', include('students_app.urls')),
]
