from django.urls import include, path
from rest_framework import routers

from socializei.api.viewsets import EventoViewSet, OrganizadorViewSet

router = routers.SimpleRouter()
router.register('eventos', EventoViewSet)
router.register('organizadores', OrganizadorViewSet)

urlpatterns = [
    # path('', include())
]
