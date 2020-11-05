from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include

urlpatterns = [
    url(r'^admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('jorgeapp/', admin.site.urls),
    path('', include('website.urls')),
]
