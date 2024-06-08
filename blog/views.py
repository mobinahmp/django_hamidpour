from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    return render(request,'blog/index.html',{})

def post(request):
    return render(request,'blog/post.html',{})

def posts(request):
    posts=Post.objects.all().order_by("-created_at")
    return render(request,'blog/posts.html',{'posts':posts})

