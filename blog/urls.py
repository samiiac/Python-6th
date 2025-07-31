from django.urls import path
from . import views
urlpatterns = [
    path('',views.index_page,name='index'),
    path('blogs',views.blogs_page,name='blog-page'),
    path('blog/<str:pk>',views.blog_detail_page,name='blog-detail'),
   
]