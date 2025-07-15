from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from tasks.models import Tag, Task


class TaskListView(generic.ListView):
    model = Task
    fields = "__all__"
    template_name = "tasks/index.html"


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("index")


class ToggleCompleteTaskView(generic.DetailView):
    model = Task
    template_name = "tasks/index.html"

    def post(self, request, *args, **kwargs):
        task = Task.objects.get(pk=self.kwargs["pk"])
        task.is_done = not task.is_done
        task.save()
        return HttpResponseRedirect(reverse_lazy("index"))


class TagListView(generic.ListView):
    model = Tag
    fields = "__all__"
    queryset = Tag.objects.prefetch_related('tasks').all()
    template_name = "tasks/tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tags-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tags-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tags-list")
