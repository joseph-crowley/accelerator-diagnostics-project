from django.urls import path
from .views import (
    AnalysisHomeView,

    # Run Views
    RunListView,
    RunDetailView,
    RunCreateView,
    RunUpdateView,
    RunDeleteView,

    # DataRecord Views
    DataRecordListView,

    # Program Views
    ProgramListView,
    ProgramDetailView,
    ProgramUploadView,
    ProgramEditView,
    ProgramDeleteView,

    # Workflow Views
    WorkflowListView,
    WorkflowCreateEditView,
    WorkflowDeleteView,
    WorkflowDetailView,

    # Plot Views
    PlotListView,
    PlotDetailView,
    PlotCreateView,
    PlotEditView,
    PlotDeleteView
)

urlpatterns = [
    # Home URL
    path('', AnalysisHomeView.as_view(), name='analysis_home'),

    # Run-related URLs
    path('runs/', RunListView.as_view(), name='run_list'),
    path('runs/create/', RunCreateView.as_view(), name='run_create'),
    path('runs/<int:pk>/', RunDetailView.as_view(), name='run_detail'),
    path('runs/<int:pk>/update/', RunUpdateView.as_view(), name='run_update'),
    path('runs/<int:pk>/delete/', RunDeleteView.as_view(), name='run_delete'),

    # DataRecord-related URLs
    path('data_records/', DataRecordListView.as_view(), name='data_record_list'),

    # Program-related URLs
    path('programs/', ProgramListView.as_view(), name='program_list'),
    path('programs/upload/', ProgramUploadView.as_view(), name='program_upload'),
    path('programs/<int:program_id>/', ProgramDetailView.as_view(), name='program_detail'),
    path('programs/<int:program_id>/edit/', ProgramEditView.as_view(), name='program_edit'),
    path('programs/<int:program_id>/delete/', ProgramDeleteView.as_view(), name='program_delete'),

    # Workflow-related URLs
    path('workflows/', WorkflowListView.as_view(), name='workflow_list'),
    path('workflows/create/', WorkflowCreateEditView.as_view(), name='workflow_create'),
    path('workflows/<int:workflow_id>/', WorkflowDetailView.as_view(), name='workflow_detail'),
    path('workflows/<int:workflow_id>/edit/', WorkflowCreateEditView.as_view(), name='workflow_edit'),
    path('workflows/<int:workflow_id>/delete/', WorkflowDeleteView.as_view(), name='workflow_delete'),

    # Plot-related URLs
    path('plots/', PlotListView.as_view(), name='plot_list'),
    path('plots/create/', PlotCreateView.as_view(), name='plot_create'),
    path('plots/<int:plot_id>/', PlotDetailView.as_view(), name='plot_detail'),
    path('plots/<int:plot_id>/edit/', PlotEditView.as_view(), name='plot_edit'),
    path('plots/<int:plot_id>/delete/', PlotDeleteView.as_view(), name='plot_delete'),
]
