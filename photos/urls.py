from django.conf.urls import url
from photos.views import HomeView, PhotoDetailView, PhotoCreationView, PhotoListView


urlpatterns = [
    url(r'^create$', PhotoCreationView.as_view(), name='photos_create'),
    url(r'^photos/$', PhotoListView.as_view(), name='photos_my_photos'),
    url(r'^photos/(?P<pk>\d+)$', PhotoDetailView.as_view(), name='photos_detail'), # \d Patrón para uno o más números
    url(r'^$', HomeView.as_view(), name='photos_home')
]