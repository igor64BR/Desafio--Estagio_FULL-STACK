from django.urls import include, path
from rest_framework import routers

from socializei.api.viewsets import EventoViewSet, OrganizadorViewSet
from socializei.views import index, organizador_form, evento_form, evento_detail

router = routers.SimpleRouter()
router.register('eventos', EventoViewSet)
router.register('organizadores', OrganizadorViewSet)

urlpatterns = [
    path('', index, name='indice'),
    path('evento/', evento_form, name='evento'),
    path('evento/<int:pk>', evento_detail, name='evento_detail'),
    path('organizador/', organizador_form, name='organizador')
]
