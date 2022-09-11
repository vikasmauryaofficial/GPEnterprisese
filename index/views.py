from operator import index
from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse
from. models import *
# Create your views here.
def index(request):
    dic={}
    obj=Category.objects.all()
    dic["categ"]=obj
    return render(request,"index.html",dic)
def about(request):
    return render(request,"about.html")
def blog_sidebar(request):
    return render(request,"blog_sidebar.html")
def blog_single(request):
    return render(request,"blog_single.html")
def blog(request):
    return render(request,"blog.html")
def contact(request):
    return render(request,"contact.html")
def course_single(request):
    return render(request,"course_single.html")
def course(request):
    dic={}
    obj=service.objects.all()
    dic["ser"]=obj
    return render(request,"course.html",dic)
def pricing(request):
    return render(request,"pricing.html")
def register(request):
    return render(request,"register.html")
def services(request):
  

    return render(request,"service.html")
def trainer(request):
    return render(request,"trainer.html")
