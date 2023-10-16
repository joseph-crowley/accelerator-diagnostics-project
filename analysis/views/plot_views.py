from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from analysis.forms import PlotForm
from analysis.models import Plot

from django.forms import modelformset_factory
from analysis.forms import PlotForm, RunDataFormSet, CutFormSet  # Assuming you have these forms defined.

class PlotCreateView(LoginRequiredMixin, CreateView):
    model = Plot
    form_class = PlotForm
    template_name = 'plot_form.html'
    success_url = reverse_lazy('analysis_home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        if self.request.POST:
            context['run_data_formset'] = RunDataFormSet(self.request.POST, prefix='rundata')
            context['cut_formset'] = CutFormSet(self.request.POST, prefix='cut')
        else:
            context['run_data_formset'] = RunDataFormSet(prefix='rundata')
            context['cut_formset'] = CutFormSet(prefix='cut')

        return context

    def form_valid(self, form):
        context = self.get_context_data()
        run_data_formset = context['run_data_formset']
        cut_formset = context['cut_formset']

        if run_data_formset.is_valid() and cut_formset.is_valid():
            # First save this main form instance to get the id
            self.object = form.save()
            
            # Then use that instance to save the related formsets
            run_data_formset.instance = self.object
            cut_formset.instance = self.object
            
            run_data_formset.save()
            cut_formset.save()

            return super().form_valid(form)
        else:
            return self.form_invalid(form)

class PlotEditView(LoginRequiredMixin, UpdateView):
    model = Plot
    form_class = PlotForm
    pk_url_kwarg = 'plot_id'
    template_name = 'plot_form.html'
    success_url = reverse_lazy('analysis_home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        if self.request.POST:
            context['run_data_formset'] = RunDataFormSet(self.request.POST, prefix='rundata', instance=self.object)
            context['cut_formset'] = CutFormSet(self.request.POST, prefix='cut', instance=self.object)
        else:
            context['run_data_formset'] = RunDataFormSet(prefix='rundata', instance=self.object)
            context['cut_formset'] = CutFormSet(prefix='cut', instance=self.object)

        return context

    def form_valid(self, form):
        context = self.get_context_data()
        run_data_formset = context['run_data_formset']
        cut_formset = context['cut_formset']

        if run_data_formset.is_valid() and cut_formset.is_valid():
            # First save this main form instance to get the id
            self.object = form.save()
            
            # Then use that instance to save the related formsets
            run_data_formset.instance = self.object
            cut_formset.instance = self.object
            
            run_data_formset.save()
            cut_formset.save()

            return super().form_valid(form)
        else:
            return self.form_invalid(form)

class PlotDeleteView(LoginRequiredMixin, DeleteView):
    model = Plot
    pk_url_kwarg = 'plot_id'
    template_name = 'plot_confirm_delete.html'
    success_url = reverse_lazy('analysis_home')

class PlotListView(LoginRequiredMixin, ListView):
    model = Plot
    template_name = 'plot_list.html'
    context_object_name = 'plots'

class PlotDetailView(LoginRequiredMixin, DetailView):
    model = Plot
    template_name = 'plot_detail.html'
    pk_url_kwarg = 'plot_id'
    context_object_name = 'plot'
