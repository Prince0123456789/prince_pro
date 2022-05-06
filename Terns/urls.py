"""Terns URL Configuration

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
from django.urls import path,include

from shop.views import del_user, index, login, loginvalidate, logout, newuser, product, saveuser, signup, users

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/login/',login),
    path('signup/', signup),
    path('saveuser/', saveuser),
    path('users/', users),
    path('loginvalidate/',loginvalidate),
    path('logout/', logout),
    path('delete/', del_user),
    path('newuser/',newuser),
    path('account/',include('django.contrib.auth.urls')),
    # shop links
    path('',index),
    path('product/',product),
]
