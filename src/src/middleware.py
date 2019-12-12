# -*- coding: utf-8 -*-


class InfoMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            try:
                request.user = request.user
                request.usuario = request.user.usuario
            except AttributeError:
                request.user = False
                request.usuario = False

        return self.get_response(request)
