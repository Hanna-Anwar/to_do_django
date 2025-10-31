"""
URL configuration for todo_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from user_app.views import *

from task_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('register/',RegistrationView.as_view(),name="register"),

    path('login/',LoginView.as_view(),name="login"),

    path('logout/',LogoutView.as_view(),name="logout"),

    path('addtask/',TaskAddView.as_view(),name="add_task"),

    path('tasklisting/',TaskListView.as_view(),name="listtask"),

    path('taskupdate/<int:pk>',TaskUpdateView.as_view(),name="updatetask"),

    path('deletetask/<int:pk>',TaskDeleteView.as_view(),name="delete"),

    path("",HomeView.as_view(),name="home"),

    path('taskcomplete/<int:pk>',TaskCompleteView.as_view(),name="complete"),
]
