import os
from django.http import HttpResponse
from django.views import View
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from web.models import TopsisResult, ScoreRaw
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.models import Sum
import web.topsisAutomation as tp
import pandas as pd
import json

class HelloView(View):
    def get(self, request):
        return HttpResponse('Hello, World!')

@method_decorator(csrf_exempt, name='dispatch')
class TopsisAutomationView(View):
    def get(self, request):
        data = TopsisResult.objects.all()
        data_list = list(data.values('rank', 'name', 'score'))
        data_json = json.dumps(data_list, cls=DjangoJSONEncoder)
        # data_json = serializers.serialize('json', data, fields=('rank', 'name', 'score'))
        return HttpResponse(data_json, content_type='application/json')
    def post(self, request):
        csv_file = request.FILES.get('file')
        sample_size = int(request.POST.get('sample_size'))

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

        df_new = pd.read_csv(csv_file)
        df_main = None

        if os.path.exists('web/data/data.csv'):
            df_main = pd.read_csv('web/data/data.csv')

            total_sample_size = ScoreRaw.objects.aggregate(sum_sample_size=Sum('sample_size'))['sum_sample_size']
            if not total_sample_size:
                total_sample_size = 0
            total_sample_size = int(total_sample_size)

            df_main.iloc[:, 1:] = df_main.iloc[:, 1:]*total_sample_size/(total_sample_size+sample_size)
            for i in range (len(df_new)):
                social_media = df_new.iloc[i, 0]
                df_main.loc[df_main['Alternatif'] == social_media, df_main.columns[1:]] += df_new.iloc[i, 1:]*sample_size/(total_sample_size+sample_size)
        else:
            df_main = df_new

        df_main.to_csv('web/data/data.csv', index=False)
        with open(full_path, 'wb+') as destination:
            for chunk in csv_file.chunks():
                destination.write(chunk)

        ScoreRaw.objects.create(path=f'/static/data/{csv_file.name}', sample_size=sample_size)

        auto = tp.TopsisAutomation("web/data/data.csv", [0.4, 0.4, 0.2], [1, 1, 1])
        auto.calculateTopsis()
        auto.persist_result()

        return HttpResponse('File uploaded successfully')