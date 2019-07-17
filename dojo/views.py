import os
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def mysum(request, numbers):
    result = sum(map(lambda s: int(s or 0),numbers.split('/')))
    return HttpResponse(result)

def hello(request, name, age):
    return HttpResponse('안녕하세요. {}. {}살이시네요.'.format(name,age))

def post_list1(request):
    name = "범수"
    return HttpResponse('''
    <h1>AskDjango</h1>
    <p>{name}</p>
    <p>나는 최범수다</P>
    '''.format(name=name))

def post_list2(request):
    name = "범수"
    return render(request, 'dojo/post_list.html', {'name':name})

def post_list3(request):
    return JsonResponse({
        'massage' : "안녕 파이썬&장고",
        'items' : ['Python', 'Django', 'Celery', 'Azure', 'AWS']
    }, json_dumps_params={'ensure_ascii':False})

def excel_download(request):
    filepath = os.path.join(settings.BASE_DIR, 'example.xlsx')
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response