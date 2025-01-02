from django.contrib import admin #For admin thing
from django.contrib.auth import views as auth_views# For Login things
from django.urls import path, include # For all of them

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lessons/', include('lessons.urls')),
]
