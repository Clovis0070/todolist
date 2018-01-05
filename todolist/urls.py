"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from todo import views

urlpatterns = [
    url(r'^admin', admin.site.urls),
    # url(r'(?!admin)', include('todo.urls'))
    # url(r'', include('todo.urls'))
    url(r'^$', views.index),
    url(r'^complete/(?P<pk>\d+)/', views.complete),
    url(r'^delete/(?P<pk>\d+)/', views.delete),    # 匹配正则，并将数字保存在pk中，传入views.delete方法作为参数。 注意（?P<name>...)的正则用法是：匹配...的内容，并将其保存到name变量里。

]
