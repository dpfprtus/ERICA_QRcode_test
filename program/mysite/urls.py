"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
    path('', include('polls.urls')),
]
from django.urls import path
from polls import views
"""
path() : 이 함수는 route, view 2개의 필수 인자와, kwargs, name 2개의 선택 인자를 받는다.
    route : URL 패턴 표현하는 문자열
    view : URL 스트링이 매칭되면 호출되는 뷰 함수이다. 
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
]
