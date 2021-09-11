from django.urls import include, path
from rest_framework import routers

from socializei.api.viewsets import EventoViewSet, OrganizadorViewSet
from socializei.views import index, organizador_form, evento_form, evento_detail, delete_evento, delete_organizador

router = routers.SimpleRouter()
router.register('eventos', EventoViewSet)
router.register('organizadores', OrganizadorViewSet)

urlpatterns = [
    path('', index, name='indice'),
    path('evento/', evento_form, name='evento'),
    path('evento/<int:pk>', evento_detail, name='evento_detail'),
    path('organizador/', organizador_form, name='organizador'),
    path('evento/<int:pk>/delete/', delete_evento, name='deletar_evento'),
    path('organizador/<int:pk>/delete/', delete_organizador, name='deletar_organizador')
]
