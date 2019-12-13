# -*- coding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.db import transaction
from .forms import JuntaForm
from .models import Junta, Monedero, ParticipanteJunta


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'plataforma/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['juntas'] = Junta.objects.filter(activo=True)
        return context


class MonederoView(LoginRequiredMixin, TemplateView):
    template_name = 'plataforma/monedero.html'

    def get_context_data(self, *args, **kwargs):
        context = super(MonederoView, self).get_context_data(*args, **kwargs)
        print(self.request.user.id)
        context['monedero'] = Monedero.objects.get(usuario_id=self.request.user.id)
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
        context['juntas'] = Junta.objects.filter(creador_id=self.request.user.id)
        return context


class MisJuntasView(LoginRequiredMixin, TemplateView):
    template_name = 'plataforma/juntas.html'

    def get_context_data(self, *args, **kwargs):
        context = super(MisJuntasView, self).get_context_data(*args, **kwargs)
        context['juntas'] = Junta.objects.filter(creador_id=self.request.user.id)
        return context


class CrearJuntasView(LoginRequiredMixin, TemplateView):
    template_name = 'plataforma/crear_junta.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CrearJuntasView, self).get_context_data(*args, **kwargs)
        context['forms'] = JuntaForm()
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        forms = JuntaForm(request.POST)
        if forms.is_valid():

            monto = forms.cleaned_data["monto"]
            nro_cuotas = forms.cleaned_data["nro_cuotas"]
            cuota = monto/nro_cuotas
            participantes = nro_cuotas

            with transaction.atomic():
                junta = forms.save(commit=False)
                junta.creador_id = request.user.id
                junta.nro_participantes = participantes
                junta.activo = True
                junta.abierto = True
                junta.save()
                participante_junta = ParticipanteJunta()
                participante_junta.junta = junta
                participante_junta.participante_id = request.user.id
                participante_junta.monto = monto
                participante_junta.nro_cuotas = nro_cuotas
                participante_junta.cuota = cuota
                participante_junta.es_creador = True
                participante_junta.save()

            url = reverse('yunta:juntas')
            return HttpResponseRedirect(url)
        else:
            context.update({
                'forms': forms
            })
            return render(request, self.template_name, context)


class ReportesView(LoginRequiredMixin, TemplateView):
    template_name = 'plataforma/reportes.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ReportesView, self).get_context_data(*args, **kwargs)
        return context
