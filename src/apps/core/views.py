from django.shortcuts import render
# from django.urls import reverse_lazy

from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# from .models import Object


class HomeView(TemplateView):
    template_name = 'base.html'


# class ObjectListView(ListView):
#     model = Object
#     template_name = 'core/object/object_list.html'
#     context_object_name = 'object'


# class ObjectDetailView(DetailView):
#     model = Object
#     template_name = 'core/object/object_detail.html'
#     context_object_name = 'object'


# class ObjectCreateView(CreateView):
#     model = Object
#     template_name = 'core/object/object_form.html'
#     fields = '__all__'


# class ObjectUpdateView(UpdateView):
#     model = Object
#     template_name = 'core/object/object_form.html'
#     fields = '__all__'


# class ObjectDeleteView(DeleteView):
#     model = Object
#     template_name = 'core/object/object_delete.html'
#     context_object_name = 'object'
#     success_url = reverse_lazy('object_list')
