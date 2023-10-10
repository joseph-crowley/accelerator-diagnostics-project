# docs/views/docs_views.py

from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from docs.models import Documentation
from docs.forms import DocumentationForm

class DocumentationListView(View):
    def get(self, request):
        # sort docs by date of creation
        docs = Documentation.objects.all().order_by('-date_created')
        return render(request, 'documentation_list.html', {'object_list': docs})

class DocumentationDetailView(View):
    def get(self, request, pk):
        doc = get_object_or_404(Documentation, pk=pk)
        all_docs = Documentation.objects.all().order_by('-date_created')
        return render(request, 'documentation_detail.html', {'object': doc, 'all_docs': all_docs})

@method_decorator(login_required, name='dispatch')
class DocumentationCreateView(View):
    def get(self, request):
        form = DocumentationForm()
        return render(request, 'documentation_form.html', {'form': form})

    def post(self, request):
        form = DocumentationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('documentation_list'))
        return render(request, 'documentation_form.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class DocumentationUpdateView(View):
    def get(self, request, pk):
        doc = get_object_or_404(Documentation, pk=pk)
        form = DocumentationForm(instance=doc)
        return render(request, 'documentation_form.html', {'form': form})

    def post(self, request, pk):
        doc = get_object_or_404(Documentation, pk=pk)
        form = DocumentationForm(request.POST, instance=doc)
        if form.is_valid():
            form.save()
            return redirect(reverse('documentation_list'))
        return render(request, 'documentation_form.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class DocumentationDeleteView(View):
    def get(self, request, pk):
        doc = get_object_or_404(Documentation, pk=pk)
        return render(request, 'documentation_confirm_delete.html', {'object': doc})

    def post(self, request, pk):
        doc = get_object_or_404(Documentation, pk=pk)
        doc.delete()
        return redirect(reverse('documentation_list'))
