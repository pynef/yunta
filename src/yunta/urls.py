from django.urls import path
from .views import (
    HomeView, MonederoView, CronogramaView, CrearJuntasView, ReportesView, MisJuntasView, JuntaViews
)
from .ajax import clave_junta
app_name = 'yunta'

urlpatterns = [
    path('ajax/clave_junta', clave_junta, name='clave_junta'),

    path('home', HomeView.as_view(), name='home'),
    path('junta/<int:junta_id>/', JuntaViews.as_view(), name='junta'),
    path('mis_juntas', MisJuntasView.as_view(), name='mis_juntas'),

    path('monedero', MonederoView.as_view(), name='monedero'),
    path('cronograma', CronogramaView.as_view(), name='cronograma'),
    path('crear_junta', CrearJuntasView.as_view(), name='crear_junta'),
    path('reportes', ReportesView.as_view(), name='reportes'),
]
