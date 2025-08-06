from django.shortcuts import render
from .models import Blog
from django.views import generic
from django.views.generic import ListView
# Create your views here.

def index_page(request):
    
    return render(request, "index.html")


# def blogs_page(request):
#     blogs = Blog.objects.all()
#     return render(request, "blogs.html",{
#         'blogs': blogs
#     })


# def blog_detail_page(request,pk):
#     blog_detail = Blog.objects.get(pk = pk)
#     return render(request, "blog-details.html",{
#         'blog_detail':blog_detail
#     })
    
class BlogView(ListView):
    model = Blog
    template_name = 'blogs.html'
  
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object-list'] = Blog.objects.all()
        return context
    
class BlogCreateView(generic.CreateView):
    template_name = 'blog_commons/form.html'
    queryset = Blog.objects.all()
    fields = "__all__"
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        return data
    
class BlogReadView(generic.ListView):
   template_name = 'blog-details.html'
   queryset = Blog.objects.all()
   fields = "__all__"
   context_object_name = 'object_list'
   
   def get_context_data(self, **kwargs):
      data = super().get_context_data(**kwargs)
      return data
    
class BlogUpdateView(generic.UpdateView):
    template_name = 'blog_commons/form.html'
    queryset = Blog.objects.all()
    fields = "__all__"
    
    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        return data
    
class BlogDeleteView(generic.DeleteView):
    template_name = 'blog_commons/form.html'
    queryset = Blog.objects.all()
    
    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        return data