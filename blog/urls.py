from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index_page,name='index'),
    # path('blogs',views.blogs_page,name='blog-page'),
    # path('blog/<str:pk>',views.blog_detail_page,name='blog-detail'),
   
]

urlpatterns += [
    path("blogs/",include(
        [
            path("",views.BlogView.as_view(),name='read-bloglist'),
            path("details/str:pk>/",views.BlogReadView.as_view(),name='blogdetails'),
            path("create/",views.BlogCreateView.as_view(),name='create-blog'),
            path("delete/<str:pk>/",views.BlogDeleteView.as_view(),name='delete-blog'),
            path("update/<str:pk>/",views.BlogCreateView.as_view(),name='update-blog')
       
        ]
    ))
]