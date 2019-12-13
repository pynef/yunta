# -*- coding: utf-8 -*-
from .models import Junta, Monedero, ParticipanteJunta, Usuario


def agregar_participante_junta(junta_id, user_id):
    response = {'error': False, 'data': '', 'mensaje': ''}
    try:
        junta = Junta.objects.get(id=junta_id)
        # calculos
        monto = junta.monto
        nro_cuotas = junta.nro_cuotas
        cuota = monto / nro_cuotas
        # crear
        participante_junta = ParticipanteJunta()
        participante_junta.junta = junta
        participante_junta.participante_id = user_id
        participante_junta.monto = junta.monto
        participante_junta.nro_cuotas = junta.nro_cuotas
        participante_junta.cuota = cuota
        participante_junta.mi_cuota = cuota
        participante_junta.save()

        if junta.nro_cuotas == ParticipanteJunta.objects.filter(junta_id=junta.id).count():
            junta.abierto = False
            junta.save()

        response = {'error': False, 'data': participante_junta.id, 'mensaje': 'todo correcto'}
    except Exception as error:
        message = "{}".format(error)
        response = {'error': True, 'data': '', 'mensaje': message}
    return response
