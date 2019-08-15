import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class JsonResponseMixin(object):
    def get_json_context(self, context):
        # transforms initial context data to json
        json_context = context  #add code to transform
        return json_context


    def render_to_json_response(self, context, **response_kwargs):
        '''returns a json formatted response'''
        return JsonResponse(self.get_json_context(context), **response_kwargs)

class CSRFExemptMixin(object):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)