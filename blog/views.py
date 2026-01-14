from django.shortcuts import render
from .models import Haqda,Mahsulot,Reklama
from user.models import Coment
from django.views.generic import CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    title = "Beoutifil"
    about = Haqda.objects.all().first()
    maxsulotlar = Mahsulot.objects.all()
    reklama = Reklama.objects.all()
    coment = Coment.objects.all()
    malumot = {
        "title":title,
        'haqda':about,
        "pro":maxsulotlar,
        "r":reklama,
        "c":coment
    }
    return render(request,'index.html',context=malumot)
def about(request):
    title = "About"
    malumot = {
        "title":title
    }
    return render(request,'about.html',context=malumot)
def client(request):
    title = "Client"
    malumot = {
        "title":title
    }
    return render(request, 'client.html',context=malumot)
def products(request):
    title = "Products"
    malumot = {
        "title":title
    }
    return render(request,'products.html',context=malumot)
def contact(request):
    title = "Contact"
    malumot = {
        "title":title
    }
    return render(request,'contact.html',context=malumot)

@login_required
def detail(request,id):
    title = "Detail"
    mahsulot = Mahsulot.objects.get(id=id)
    malumot = {
        "title":title,
        'p':mahsulot,
    }
    return render(request,'detail.html',context=malumot)
class MahsulotCreate(CreateView):
    model = Mahsulot
    template_name = 'crud/create.html'
    success_url = '/'
    fields = ['neme','text','img','narx']

class MahsulotUpdate(UpdateView):
    model = Mahsulot
    template_name = 'crud/update.html'
    success_url = '/'
    fields = ['neme','text','img','narx']

class MahsulotDelete(DeleteView):
    model = Mahsulot
    template_name = 'crud/delete.html'
    success_url = '/'
    fields = ['name','text','img','narx']
