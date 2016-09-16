from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from files.views import FileViewSet
from photos import urls as photos_urls
from users import urls as users_urls


router = DefaultRouter()
router.register('api/1.0/files', FileViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include(photos_urls)),
    url(r'', include(users_urls)),
    url(r'', include(router.urls))
]
