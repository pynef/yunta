# -*- coding: utf-8 -*-
import datetime
from django.http import JsonResponse

from .models import Junta
from .functions import agregar_participante_junta


def clave_junta(request):
    response = {'error': False, 'correct': False, 'data': '', 'mensaje': ''}
    user_id = request.GET.get('user_id')
    junta_id = request.GET.get('junta_id')
    junta_clave = request.GET.get('junta_clave')
    junta = Junta.objects.filter(id=junta_id, clave=junta_clave)

    if junta.count():
        response = agregar_participante_junta(junta_id, user_id)
        response.update({'correct': True})
        print(response)
    else:
        response.update({'message': "Error en la contraseña!!!"})

    return JsonResponse(response)
