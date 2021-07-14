"""ISEEK_SYSTEM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('pages.urls')),
    # path('products/', product_detail_view),
    #path('create/', product_create_view),
    # path('blog/', include('blog.urls')),
    path('', include('search.urls')),
    #path('blog/create', article_create_view),
    #path('blog/', article_list_view),
    #path('products/<int:product_id>/', product_detail_view, name='product'),
    #path('products/', product_list_view, name='product-list'),
    #path('products/<int:product_id>/delete/', product_delete_view, name='product-delete')
]
