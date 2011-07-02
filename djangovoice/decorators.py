# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.utils import simplejson as json

def apply_only_xhr(original_function):
    def decorated(request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponse(status=403)

        return original_function(request, *args, **kwargs)

    return decorated

def return_json(original_function):
    def decorated(request, *args, **kwargs):
        response = original_function(request, *args, **kwargs)
        if not response:
            response = {'errors': True}
        else:
            response.update({'errors': False})

        data = json.dumps(response, indent=None).encode('utf-8')

        return HttpResponse(data, 'application/json')

    return decorated
