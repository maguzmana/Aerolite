from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]

# Rutas para los archivos estáticos en desarrollo
urlpatterns += staticfiles_urlpatterns()

# Rutas para los archivos estáticos en producción
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)