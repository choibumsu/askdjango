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
    
class DetailView(object):
    def __init__(self, model):
        self.model = model

    def get_object(self, *args, **kwargs):
        return get_object_or_404(self.model, pk=kwargs['pk'])

    def get_template_name(self):
        return f'{self.model._meta.app_label}/{self.model._meta.model_name}_detail.html'
        
    def dispatch(self, request, *args, **kwargs):
        return render(request, self.get_template_name(), {
            self.model._meta.model_name: self.get_object(*args, **kwargs),
        })
    @classmethod
    def as_view(cls, model):
        def view(request, *args, **kwargs):
            self = cls(model)
            return self.dispatch(request, *args, **kwargs)
        return view
    

post_detail = DetailView.as_view(Post)