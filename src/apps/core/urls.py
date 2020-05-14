from django.urls import path
from .views import (
    HomeView,
    # ObjectListView, ObjectDetailView, ObjectCreateView, ObjectUpdateView, ObjectDeleteView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    # path('object/', ObjectListView.as_view(), name='object_list'),
    # path('object/<int:pk>/', ObjectDetailView.as_view(), name='object_detail'),
    # path('object/create/', ObjectCreateView.as_view(), name='object_create'),
    # path('object/update/<int:pk>/',
    #      ObjectUpdateView.as_view(), name='object_update'),
    # path('object/delete/<int:pk>/',
    #      ObjectDeleteView.as_view(), name='object_delete'),
]
