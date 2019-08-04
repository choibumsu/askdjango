import os
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Account, Post

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

def form_prac(request):
    rqst = request.POST
    context = {
        'ctx' : rqst,
    }
    return render(request, "dojo/example.html", context)

def account_list(request):
    accounts = Account.objects.all()
    return render(request, "dojo/account_list.html", {'accounts':accounts})

def account_detail(request, pk):
    account = get_object_or_404(Account, pk=pk)
    posts = Post.objects.filter(author_name = account.name)
    return render(request, "dojo/account_detail.html", {'account':account, 'posts':posts})


def account_create(request):
    if request.method == "POST":
        account = Account()
        account.name = request.POST['name']
        account.age = request.POST['age']
        account.save()

        accounts = Account.objects.all()
        return render(request, "dojo/account_list.html", {'accounts':accounts})    
    else:
        return render(request, "dojo/account_create.html")
    
def post_list(request):
    posts = Post.objects.all()
    return render(request, "dojo/post_list.html", {'posts':posts})

def post_create(request):
    if request.method == "POST":
        post = Post()
        post.author_name = request.POST['author_name']
        post.title = request.POST['title']
        post.text = request.POST['text']
        post.save()

        posts = Post.objects.all()
        return render(request, "dojo/post_list.html", {'posts':posts})
    else:
        return render(request, "dojo/post_create.html")
    
def generate_view_fn(model):
    def view_fn(request, pk):
        instance = get_object_or_404(model, pk=pk)
        instance_name = model._meta.model_name
        template_name = f'{model._meta.app_label}/{instance_name}_detail.html'
        return render(request, template_name, {
            instance_name: instance,
        })
    return view_fn


post_detail = generate_view_fn(Post)