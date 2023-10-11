from django.views import View
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect, get_object_or_404
from analysis.forms import PlotForm
from analysis.models import Plot

# View to create a new plot
@method_decorator(login_required, name='dispatch')
class PlotCreateView(View):
    def get(self, request):
        form = PlotForm()
        return render(request, 'plot_form.html', {'form': form})

    def post(self, request):
        form = PlotForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('analysis_home'))  # Redirect to a relevant page
        return render(request, 'plot_form.html', {'form': form})

# View to edit a plot
@method_decorator(login_required, name='dispatch')
class PlotEditView(View):
    def get(self, request, plot_id):
        plot = get_object_or_404(Plot, pk=plot_id)
        form = PlotForm(instance=plot)
        return render(request, 'plot_form.html', {'form': form})

    def post(self, request, plot_id):
        plot = get_object_or_404(Plot, pk=plot_id)
        form = PlotForm(request.POST, instance=plot)
        if form.is_valid():
            form.save()
            return redirect(reverse('analysis_home'))
        
        return render(request, 'plot_form.html', {'form': form})

# View to delete a plot
@method_decorator(login_required, name='dispatch')
class PlotDeleteView(View):
    def get(self, request, plot_id):
        plot = get_object_or_404(Plot, pk=plot_id)
        return render(request, 'plot_confirm_delete.html', {'plot': plot})

    def post(self, request, plot_id):
        plot = get_object_or_404(Plot, pk=plot_id)
        plot.delete()
        return redirect(reverse('analysis_home'))
    
# View to list all plots
@method_decorator(login_required, name='dispatch')
class PlotListView(View):
    def get(self, request):
        plots = Plot.objects.all()
        return render(request, 'plot_list.html', {'plots': plots})
    
# View to view a plot
@method_decorator(login_required, name='dispatch')
class PlotView(View):
    def get(self, request, plot_id):
        plot = get_object_or_404(Plot, pk=plot_id)
        return render(request, 'plot_detail.html', {'plot': plot})