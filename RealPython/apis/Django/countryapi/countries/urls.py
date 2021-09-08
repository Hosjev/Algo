from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CountryViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r"countries", CountryViewSet)


urlpatterns = [
    path("", include(router.urls))
]
