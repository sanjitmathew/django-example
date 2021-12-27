"""first_project URL Configuration

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

from django.urls import path
from first_app import views

app_name = 'first_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('user_login/', views.user_login, name='user_login'),
    path('register/', views.register_user, name='register_user'),
    path('insertwebpage/', views.insert_webpage, name='insert_webpage'),
    path('login/', views.show_login, name='show_login'),
    path('records/', views.show_records, name='show_records'),
    path('validatelogin/', views.validate_login, name='validate_login'),

]
