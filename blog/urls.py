"""blog URL Configuration

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
# from django.contrib import admin
from django.urls import path
from rest_framework.authtoken import views
from account.views import CustomAuthToken,user_Register,test_auth,user_crud
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('apia/', views.obtain_auth_token),
    path('apim/', CustomAuthToken.as_view()),
    path('usereg/', user_Register.as_view()),
    path('tes/',test_auth),
    path('user/<int:id>',user_crud.as_view())
]
