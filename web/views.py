from django.http import HttpResponse
from django.views import View
from django.core import serializers
from web.models import TopsisResult

class HelloView(View):
    def get(self, request):
        return HttpResponse('Hello, World!')

class TopsisAutomationView(View):
    def get(self, request):
        data = TopsisResult.objects.all()
        data_json = serializers.serialize('json', data)
        return HttpResponse(data_json, content_type='application/json')
