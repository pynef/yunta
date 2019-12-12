# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import JuntaForm


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'plataforma/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        return context


class MonederoView(LoginRequiredMixin, TemplateView):
    template_name = 'plataforma/monedero.html'

    def get_context_data(self, *args, **kwargs):
        context = super(MonederoView, self).get_context_data(*args, **kwargs)
        return context


class CronogramaView(LoginRequiredMixin, TemplateView):
    template_name = 'plataforma/cronograma.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CronogramaView, self).get_context_data(*args, **kwargs)
        return context


class JuntasView(LoginRequiredMixin, TemplateView):
    template_name = 'plataforma/juntas.html'

    def get_context_data(self, *args, **kwargs):
        context = super(JuntasView, self).get_context_data(*args, **kwargs)
        return context


class CrearJuntasView(LoginRequiredMixin, TemplateView):
    template_name = 'plataforma/crear_junta.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CrearJuntasView, self).get_context_data(*args, **kwargs)
        # context['forms'] = JuntaForm()
        return context


class ReportesView(LoginRequiredMixin, TemplateView):
    template_name = 'plataforma/reportes.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ReportesView, self).get_context_data(*args, **kwargs)
        return context
