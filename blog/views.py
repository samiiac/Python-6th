from django.shortcuts import render
from .models import Blog
from django.views import generic
# Create your views here.

def index_page(request):
    
    return render(request, "index.html")


def blogs_page(request):
    blogs = Blog.objects.all()
    return render(request, "blogs.html",{
        'blogs': blogs
    })


def blog_detail_page(request,pk):
    blog_detail = Blog.objects.get(pk = pk)
    return render(request, "blog-details.html",{
        'blog_detail':blog_detail
    })
    
class BlogView(generic.TemplateView):
    template_name = 'blogs.html'
    
class CreateBlogView(generic.CreateView):
    pass
    
    