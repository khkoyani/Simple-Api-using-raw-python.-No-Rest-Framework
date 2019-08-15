from updates.models import Update
from updates.forms import UpdateForm
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from testapi.mixins import CSRFExemptMixin
import json


class UpdateJsonDetailView(CSRFExemptMixin, View):
    def get(self, request, id, *args, **kwargs):
        try:
            json_obj = Update.serializeobj.get(id=id).serialize()
            return HttpResponse(json_obj, content_type='application/json')
        except Update.DoesNotExist:
            return JsonResponse('Item does not exist', safe=False)

    def put(self, request, id, *args, **kwargs):
        try:
            # json_obj = Update.serializeobj.get(id=id).serialize()
            return HttpResponse({}, content_type='application/json')
        except Update.DoesNotExist:
            return JsonResponse('Item does not exist', safe=False)

    def delete(self, request, id, *args, **kwargs):
        try:
            # json_obj = Update.serializeobj.get(id=id).serialize()
            return HttpResponse({}, content_type='application/json')
        except Update.DoesNotExist:
            return JsonResponse('Item does not exist', safe=False)


class UpdateJsonListView(CSRFExemptMixin, View):
    def get(self, request, *args, **kwargs):
        json_list = Update.serializeobj.all().serialize()
        return HttpResponse(content=json_list, content_type='application/json')

    def post(self, request, *args, **kwargs):
        form = UpdateForm(request.POST)
        if form.is_valid():
            data = form.save(commit=True).serialize()
            return HttpResponse(data, content_type='application/json', status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return HttpResponse(data, content_type='application/json', status=400)

        data = json.dumps({'message': 'No post data'})
        return HttpResponse(data, content_type='application/json', status=400)

    def delete(self, request, *args, **kwargs):
        data = json.dumps({'message': 'Stop trying to delete the entire list'})
        return HttpResponse(data, content_type='application/json', status=403)