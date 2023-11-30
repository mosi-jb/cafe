"""
URL configuration for cafe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from django.conf import settings
from django.conf.urls.static import static

admin_urls = [
    path('admin/user/',
         include(('user.urls.admin', 'cafe.user'), namespace='users-admin')),
    path('admin/media/',
         include(('media.urls.admin', 'cafe.media'), namespace='media-admin')),
    path('admin/location/',
         include(('location.urls.admin', 'cafe.location'), namespace='location-admin')),
    path('admin/menu/',
         include(('menu.urls.admin', 'cafe.menu'), namespace='menu-admin')),

]

front_urls = [
    path('front/user/',
         include(('user.urls.front', 'cafe.user'), namespace='users-front')),
    path('front/media/',
         include(('media.urls.front', 'cafe.media'), namespace='media-front')),
    path('front/location/',
         include(('location.urls.front', 'cafe.location'), namespace='location-front')),
    path('front/menu/',
         include(('menu.urls.front', 'cafe.menu'), namespace='menu-front')),

]

doc_patterns = [
    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

urlpatterns = [
                  path('akm/', admin.site.urls),
              ] + doc_patterns + admin_urls + front_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
