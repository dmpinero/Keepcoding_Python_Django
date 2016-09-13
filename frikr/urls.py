from django.conf.urls import url, include
from django.contrib import admin

from photos import urls as photos_urls
from users import urls as users_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include(photos_urls)),
    url(r'', include(users_urls))
]
