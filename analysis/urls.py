from django.urls import path
from .views import (
    RunListView, 
    RunDetailView, 
    RunCreateView, 
    RunUpdateView, 
    RunDeleteView,
    AnalysisHomeView, 
    DataRecordListView,
)

urlpatterns = [
    # Run-related URLs
    path('', AnalysisHomeView.as_view(), name='analysis_home'),
    path('runs/', RunListView.as_view(), name='run_list'),
    path('runs/<int:pk>/', RunDetailView.as_view(), name='run_detail'),
    path('runs/create/', RunCreateView.as_view(), name='run_create'),
    path('runs/<int:pk>/update/', RunUpdateView.as_view(), name='run_update'),
    path('runs/<int:pk>/delete/', RunDeleteView.as_view(), name='run_delete'),

    # DataRecord-related URLs
    path('data_records/', DataRecordListView.as_view(), name='data_record_list'),
]
