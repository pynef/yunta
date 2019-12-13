from django.urls import path
from .views import (
    HomeView, MonederoView, CronogramaView, JuntasView, CrearJuntasView, ReportesView, MisJuntasView, JuntaViews
)
from .ajax import clave_junta
app_name = 'yunta'

urlpatterns = [
    path('ajax/clave_junta', clave_junta, name='clave_junta'),

    path('home', HomeView.as_view(), name='home'),
    path('junta/<int:junta_id>/', JuntaViews.as_view(), name='paquete'),

    path('monedero', MonederoView.as_view(), name='monedero'),
    path('cronograma', CronogramaView.as_view(), name='cronograma'),
    path('juntas', JuntasView.as_view(), name='juntas'),
    path('mis_juntas', MisJuntasView.as_view(), name='mis_juntas'),
    path('crear_junta', CrearJuntasView.as_view(), name='crear_junta'),
    path('reportes', ReportesView.as_view(), name='reportes'),
]
