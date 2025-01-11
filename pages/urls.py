from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('blog/',views.blog_page_view,name='blog'),
    path('',views.home_page_view,name='home'),
]