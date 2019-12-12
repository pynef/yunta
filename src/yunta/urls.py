from django.urls import path
from .views import HomeView, MonederoView, CronogramaView, JuntasView, CrearJuntasView, ReportesView
app_name = 'yunta'

urlpatterns = [
    path('home', HomeView.as_view(), name='home'),
    path('monedero', MonederoView.as_view(), name='monedero'),
    path('cronograma', CronogramaView.as_view(), name='cronograma'),
    path('juntas', JuntasView.as_view(), name='juntas'),
    path('crear_junta', CrearJuntasView.as_view(), name='crear_junta'),
    path('reportes', ReportesView.as_view(), name='reportes'),
]
