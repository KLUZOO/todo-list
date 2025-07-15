"""
URL configuration for py_todo_list project.

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

from tasks.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    ToggleCompleteTaskView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TaskListView.as_view(), name='index'),
    path('task/create', TaskCreateView.as_view(), name='task-create'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('task/<int:pk>/toggle/', ToggleCompleteTaskView.as_view(), name='task-toggle'),
    path('tags/', TagListView.as_view(), name='tags-list'),
    path('tags/create/', TagCreateView.as_view(), name='tag-create'),
    path('tag/<int:pk>/update/', TagUpdateView.as_view(), name='tag-update'),
    path('tag/<int:pk>/delete/', TagDeleteView.as_view(), name='tag-delete'),
]
