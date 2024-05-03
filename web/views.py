import os
from django.http import HttpResponse
from django.views import View
from django.core import serializers
from web.models import TopsisResult, ScoreRaw
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class HelloView(View):
    def get(self, request):
        return HttpResponse('Hello, World!')

@method_decorator(csrf_exempt, name='dispatch')
class TopsisAutomationView(View):
    def get(self, request):
        data = TopsisResult.objects.all()
        data_json = serializers.serialize('json', data)
        return HttpResponse(data_json, content_type='application/json')
    def post(self, request):
        csv_file = request.FILES.get('file')
        sample_size = request.POST.get('sample_size')

        if not sample_size or not csv_file:
            return HttpResponse('Invalid request parameters', status=400)

        path_to_save = 'web/static/data/'
        full_path = os.path.join(path_to_save, csv_file.name)
        base, extension = os.path.splitext(csv_file.name)
        if(extension != '.csv'):
            return HttpResponse('Invalid file type', status=400)

        if os.path.exists(full_path):
            i = 1
            while os.path.exists(full_path):
                csv_file.name = f'{base} ({i}){extension}'
                full_path = os.path.join(path_to_save, csv_file.name)
                i += 1

        with open(full_path, 'wb+') as destination:
            for chunk in csv_file.chunks():
                destination.write(chunk)

        ScoreRaw.objects.create(path=f'/static/data/{csv_file.name}', sample_size=sample_size)

        return HttpResponse('File uploaded successfully')