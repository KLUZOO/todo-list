from django.shortcuts import render
from django.views import generic

from tasks.models import Tag, Task


class TaskListView(generic.ListView):
    model = Task


class TagsListView(generic.ListView):
    model = Tag
    fields = "__all__"
    queryset = Tag.objects.prefetch_related('tasks').all()
