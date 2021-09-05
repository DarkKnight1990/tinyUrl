from django.conf.urls import include, url
from django.urls import path
from django.db.models import base
from rest_framework.routers import DefaultRouter

from url_shortener.views import RedirectURL, ShortenURL

# router = DefaultRouter()
# router.register(r'data', CustomURLViewset, basename='data')
# router.register(
#     r"shorten", ShortenURL.as_view(), name="shorten"
# )

api_urls = [
    path("shorten", ShortenURL.as_view(), name="shorten"),
    # path("<path:short_url>/", RedirectURL.as_view(), name="redirect"),
]

urlpatterns = [
    path("api/v1/", include(api_urls))
]
