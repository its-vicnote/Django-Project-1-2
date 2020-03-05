from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return HttpResponse("/ placeholder to later display a list of all blogs")
def new(request):
    return HttpResponse("/ placeholder to later display a new blog")
def create(request):
    redirect("/")
def show(request, blog_id):
    return HttpResponse(f"/ placeholder to later display blog num:{blog_id}")
def edit(request, blog_id):
    return HttpResponse(f"/ placeholder to edit blog {blog_id}")
def delete(request, blog_id):
    redirect("/")

# Create your views here.
