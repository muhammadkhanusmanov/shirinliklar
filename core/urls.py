# config/urls.py (yoki loyihang nomi qanday bo‘lsa)
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token  # oddiy token login

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('polls.urls')),
    path('api/auth/', obtain_auth_token), 
]

# Media fayllar uchun (rasmlar)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
