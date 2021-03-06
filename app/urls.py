
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),
    path('calendar/', include('mycalendar.urls')),
    path('gaming/', include('gaming.urls')),
    path('studentresults/', include('reportcards.urls')),
]
