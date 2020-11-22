"""hakaton URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from hakaton_app import views
from django.views.static import serve
from hakaton.settings import STATICFILES_DIRS
urlpatterns = [
    path('admin/', admin.site.urls),
    path("map/", views.smap, name="map_view"),
    path("multi_map/", views.mmap, name="mmap_view"),
    path("", views.index, name="index"),
    path('accounts/login/', views.login_page, name='login_page'),
    path('accounts/login_check/', views.login_check_page, name='login'),
    path('accounts/logout/', views.logout_page, name='logout'),
    path("registration/", views.registration_page, name="register"),
    path("uproblems/", views.user_problems, name="sub_prob"),
    path("create_new_problem/", views.create_problem, name="add_prob"),
    path("static/", serve, {'document_root': STATICFILES_DIRS}),
]
