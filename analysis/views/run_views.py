from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from analysis.models import Run
from analysis.forms import RunForm

@method_decorator(login_required, name='dispatch')
class RunListView(View):
    def get(self, request):
        runs = Run.objects.all().order_by('-run_id')
        return render(request, 'run_list.html', {'runs': runs})

@method_decorator(login_required, name='dispatch')
class RunDetailView(View):
    def get(self, request, pk):
        run = get_object_or_404(Run, pk=pk)
        return render(request, 'run_detail.html', {'run': run})

@method_decorator(login_required, name='dispatch')
class RunCreateView(View):
    def get(self, request):
        form = RunForm()
        return render(request, 'run_form.html', {'form': form})

    def post(self, request):
        form = RunForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('run_list'))
        return render(request, 'run_form.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class RunUpdateView(View):
    def get(self, request, pk):
        run = get_object_or_404(Run, pk=pk)
        form = RunForm(instance=run)
        return render(request, 'run_form.html', {'form': form})

    def post(self, request, pk):
        run = get_object_or_404(Run, pk=pk)
        form = RunForm(request.POST, instance=run)
        if form.is_valid():
            form.save()
            return redirect(reverse('run_detail', kwargs={'pk': pk}))
        return render(request, 'run_form.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class RunDeleteView(View):
    def get(self, request, pk):
        run = get_object_or_404(Run, pk=pk)
        return render(request, 'run_confirm_delete.html', {'run': run})

    def post(self, request, pk):
        run = get_object_or_404(Run, pk=pk)
        run.delete()
        return redirect(reverse('run_list'))
