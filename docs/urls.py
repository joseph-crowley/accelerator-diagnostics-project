# docs/urls.py

from django.urls import path
from .views import (
    DocumentationListView, 
    DocumentationDetailView, 
    DocumentationCreateView, 
    DocumentationUpdateView, 
    DocumentationDeleteView
)

urlpatterns = [
    path('', DocumentationListView.as_view(), name='documentation_list'),
    path('<int:pk>/', DocumentationDetailView.as_view(), name='documentation_detail'),
    path('new/', DocumentationCreateView.as_view(), name='documentation_create'),
    path('<int:pk>/edit/', DocumentationUpdateView.as_view(), name='documentation_edit'),
    path('<int:pk>/delete/', DocumentationDeleteView.as_view(), name='documentation_delete'),
]
