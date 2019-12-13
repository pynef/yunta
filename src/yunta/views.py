# -*- coding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.db import transaction
from .forms import JuntaForm
from django.shortcuts import get_object_or_404
from .models import Junta, Monedero, ParticipanteJunta, Usuario
import pdb


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'plataforma/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        juntas_donde_participo = sorted(set([participante_junta.junta_id for participante_junta in ParticipanteJunta.objects.filter(participante_id=self.request.user)]))
        juntas_activas = [junt.id for junt in Junta.objects.filter(activo=True, abierto=True)]
        juntas_libres = list(set(juntas_activas) - set(juntas_donde_participo))
        juntas = Junta.objects.filter(id__in=juntas_libres)
        context['juntas'] = juntas
        return context


class JuntaViews(LoginRequiredMixin, TemplateView):
    template_name = 'plataforma/junta.html'

    def get_context_data(self, *args, **kwargs):
        context = super(JuntaViews, self).get_context_data(*args, **kwargs)
        junta_id = self.kwargs.get('junta_id')
        junta = get_object_or_404(Junta, id=junta_id)
        personas = ParticipanteJunta.objects.filter(junta_id=junta_id)
        permisos = ParticipanteJunta.objects.filter(junta_id=junta_id, participante_id=self.request.user.id)
        propietario = Junta.objects.filter(id=junta_id, abierto=False, iniciar=False, creador_id=self.request.user.id)

        if junta.nro_cuotas != personas.count():
            context['habilidar_boton'] = True

        if propietario.count() > 0:
            context['iniciar'] = True
        else:
            context['iniciar'] = False

        context.update({
            'junta': junta,
            'personas': personas,
            'permisos': permisos
        })
        return context


class MisJuntasView(LoginRequiredMixin, TemplateView):
    template_name = 'plataforma/mis_juntas.html'

    def get_context_data(self, *args, **kwargs):
        context = super(MisJuntasView, self).get_context_data(*args, **kwargs)
        print(ParticipanteJunta.objects.filter(participante_id=self.request.user.id))
        context['mis_juntas'] = ParticipanteJunta.objects.filter(participante_id=self.request.user.id)
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
                participante_junta.es_activo = True
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
