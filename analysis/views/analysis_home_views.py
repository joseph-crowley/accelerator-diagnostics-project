from django.views import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class AnalysisHomeView(View):
    def get(self, request):
        functionalities = [
            {
                'title': 'Runs',
                'description': 'Initiate, monitor, and terminate data acquisition runs.',
                'links': [
                    {'url': 'run_list', 'text': 'View Runs'},
                    {'url': 'run_create', 'text': 'Start a New Run'},
                ]
            },
            {
                'title': 'Plots',
                'description': 'Create, edit, and view plots for visualizing data.',
                'links': [
                    {'url': 'plot_list', 'text': 'View Plots'},
                    {'url': 'plot_create', 'text': 'Create a Plot'},
                ]
            },
            {
                'title': 'Programs',
                'description': 'Upload, edit, and manage data analysis programs.',
                'links': [
                    {'url': 'program_list', 'text': 'View Programs'},
                    {'url': 'program_upload', 'text': 'Upload a Program'},
                ]
            },
            {
                'title': 'Workflows',
                'description': 'Create and manage workflows for data analysis.',
                'links': [
                    {'url': 'workflow_list', 'text': 'View Workflows'},
                    {'url': 'workflow_create', 'text': 'Create a Workflow'},
                ]
            },
            {
                'title': 'Data Analysis',
                'description': 'Apply filters, anomaly detection, and custom scripts to data.',
                'links': [
                    {'url': 'data_record_list', 'text': 'View Data Records'},
                ]
            }
        ]

        context = {
            'functionalities': functionalities,
        }

        return render(request, 'analysis_home.html', context)
