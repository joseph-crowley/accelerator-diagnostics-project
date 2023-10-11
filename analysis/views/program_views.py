from django.views import View
from django.views.generic import ListView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from analysis.forms import ProgramForm
from analysis.models import Program

# View to upload a new program/script
@method_decorator(login_required, name='dispatch')
class ProgramUploadView(View):
    def get(self, request):
        form = ProgramForm()
        return render(request, 'program_form.html', {'form': form})

    def post(self, request):
        form = ProgramForm(request.POST, request.FILES)
        if form.is_valid():
            program = form.save(commit=False)  # Don't save the object to the database yet
            program.created_by = request.user  # Set the created_by field to the current user
            program.save()  # Now save the object to the database
            return redirect(reverse('program_list'))  # Redirect to the list of programs
        return render(request, 'program_form.html', {'form': form})

# View to edit a program
@method_decorator(login_required, name='dispatch')
class ProgramEditView(View):
    def get(self, request, program_id):
        program = get_object_or_404(Program, pk=program_id)
        form = ProgramForm(instance=program)
        return render(request, 'program_form.html', {'form': form})

    def post(self, request, program_id):
        program = get_object_or_404(Program, pk=program_id)
        form = ProgramForm(request.POST, request.FILES, instance=program)
        if form.is_valid():
            form.save()
            return redirect(reverse('program_list'))
        
        return render(request, 'program_form.html', {'form': form})

# View to list all uploaded programs
@method_decorator(login_required, name='dispatch')
class ProgramListView(ListView):
    model = Program
    template_name = 'program_list.html'
    context_object_name = 'programs'

# View to delete a program
@method_decorator(login_required, name='dispatch')
class ProgramDeleteView(DeleteView):
    model = Program
    template_name = 'program_confirm_delete.html'
    success_url = reverse_lazy('program_list')

@method_decorator(login_required, name='dispatch')
class ProgramDetailView(View):
    def get(self, request, program_id):
        program = get_object_or_404(Program, pk=program_id)

        # Read the script file content
        script_content = ""
        try:
            with open(program.script.path, 'r') as f:
                script_content = f.read()
        except Exception as e:
            script_content = f"An error occurred while reading the script: {e}"

        context = {
            'program': program,
            'script_content': script_content
        }

        return render(request, 'program_detail.html', context)
    
    def post(self, request, program_id):
        program = get_object_or_404(Program, pk=program_id)

        # The post method could essentially be the same as the get method
        # unless you have additional logic for post requests
        script_content = ""
        try:
            with open(program.script.path, 'r') as f:
                script_content = f.read()
        except Exception as e:
            script_content = f"An error occurred while reading the script: {e}"

        context = {
            'program': program,
            'script_content': script_content
        }

        return render(request, 'program_detail.html', context)
