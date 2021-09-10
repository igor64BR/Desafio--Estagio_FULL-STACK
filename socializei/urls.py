from django.urls import include, path
from rest_framework import routers

from socializei.api.viewsets import EventoViewSet, OrganizadorViewSet
from socializei.views import index, organizadores, evento

router = routers.SimpleRouter()
router.register('eventos', EventoViewSet)
router.register('organizadores', OrganizadorViewSet)

urlpatterns = [
    path('', index, name='indice'),
    path('evento/', evento, name='evento'),
    path('organizador/', organizadores, name='organizador')
]
