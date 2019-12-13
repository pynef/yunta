# -*- coding: utf-8 -*-

from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.db import transaction
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from yunta.models import Usuario, Monedero, Junta
from yunta.forms import UserForm, UsuarioForm


class LandingView(TemplateView):
    template_name = 'landing/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(LandingView, self).get_context_data(*args, **kwargs)
        return context


class RegistrateView(TemplateView):
    template_name = 'registration/register.html'

    def get_context_data(self, *args, **kwargs):
        context = super(RegistrateView, self).get_context_data(*args, **kwargs)
        context['user_form'] = UserForm()
        context['usuario_form'] = UsuarioForm()
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        user_form = UserForm(request.POST)
        usuario_form = UsuarioForm(request.POST)

        if user_form.is_valid() and usuario_form.is_valid():

            with transaction.atomic():
                user = user_form.save()
                with transaction.atomic():
                    # creando el perfil
                    usuario = Usuario()
                    usuario.user = user
                    usuario.dni = usuario_form.cleaned_data["dni"]
                    usuario.correo = usuario_form.cleaned_data["email"]
                    usuario.nombres = usuario_form.cleaned_data["nombres"]
                    usuario.apellido_paterno = usuario_form.cleaned_data["apellido_paterno"]
                    usuario.apellido_materno = usuario_form.cleaned_data["apellido_materno"]
                    usuario.save()
                    monedero = Monedero()
                    monedero.saldo_actual = 10000
                    monedero.saldo_contable = 0
                    monedero.usuario = user
                    monedero.save()

            url = reverse('login')
            return HttpResponseRedirect(url)
        else:
            context.update({
                'user_form': user_form,
                'usuario_form': usuario_form
            })
            return render(request, self.template_name, context)
