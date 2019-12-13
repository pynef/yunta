# -*- coding: utf-8 -*-
import datetime
from django.http import JsonResponse

from .models import Junta


def clave_junta(request):
    response = {'error': False, 'correct': False, 'data': '', 'mensaje': ''}
    print(request.POST)
    junta_id = request.POST.get('junta_id')
    junta_clave = request.POST.get('junta_clave')
    junta = Junta.objects.filer(id=junta_id).update(clave=junta_clave)

    if junta.count():
        response.update({'correct': True})
    else:
        response.update({'error': True})

    return JsonResponse(response)
