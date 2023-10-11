from django.views import View
from django.views.generic import ListView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from analysis.forms import WorkflowForm
from analysis.models import Workflow

# View to create or edit a workflow
@method_decorator(login_required, name='dispatch')
class WorkflowCreateEditView(View):
    def get(self, request, workflow_id=None):
        if workflow_id:
            workflow = get_object_or_404(Workflow, pk=workflow_id)
            form = WorkflowForm(instance=workflow)
        else:
            form = WorkflowForm()
        return render(request, 'workflow_form.html', {'form': form})

    def post(self, request, workflow_id=None):
        if workflow_id:
            workflow = get_object_or_404(Workflow, pk=workflow_id)
            form = WorkflowForm(request.POST, instance=workflow)
        else:
            form = WorkflowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('workflow_list'))  # Redirect to the list of workflows
        return render(request, 'workflow_form.html', {'form': form})

# View to list all workflows
@method_decorator(login_required, name='dispatch')
class WorkflowListView(ListView):
    model = Workflow
    template_name = 'workflow_list.html'
    context_object_name = 'workflows'

# View to delete a workflow
@method_decorator(login_required, name='dispatch')
class WorkflowDeleteView(DeleteView):
    model = Workflow
    template_name = 'workflow_confirm_delete.html'
    success_url = reverse_lazy('workflow_list')

# View to view a workflow
@method_decorator(login_required, name='dispatch')
class WorkflowDetailView(View):
    def get(self, request, workflow_id):
        workflow = get_object_or_404(Workflow, pk=workflow_id)
        return render(request, 'workflow_detail.html', {'workflow': workflow})