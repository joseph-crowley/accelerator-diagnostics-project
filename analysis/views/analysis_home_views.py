from django.views import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class AnalysisHomeView(View):
    def get(self, request):
        functionalities = [
            {
                'title': 'Program Management',
                'description': 'Upload, edit, and manage your data analysis programs.',
                'links': [
                    {'url': 'program_list', 'text': 'View Programs'},
                    {'url': 'program_upload', 'text': 'Upload a Program'},
                ]
            },
            {
                'title': 'Workflow Management',
                'description': 'Create and manage workflows for data analysis.',
                'links': [
                    {'url': 'workflow_list', 'text': 'View Workflows'},
                    {'url': 'workflow_create', 'text': 'Create a Workflow'},
                ]
            },
            {
                'title': 'Plot Management',
                'description': 'Create, edit, and view plots for visualizing data.',
                'links': [
                    {'url': 'plot_list', 'text': 'View Plots'},
                    {'url': 'plot_create', 'text': 'Create a Plot'},
                ]
            },
            {
                'title': 'Run Management',
                'description': 'Initiate, monitor, and terminate data acquisition runs with ease.',
                'links': [
                    {'url': 'run_list', 'text': 'View Runs'},
                    {'url': 'run_create', 'text': 'Start a New Run'},
                ]
            },
            {
                'title': 'Data Analysis',
                'description': 'Apply filters, anomaly detection, and custom scripts to your data.',
                'links': [
                    {'url': 'data_record_list', 'text': 'View Data Records'},
                ]
            }
        ]

        how_to_use = [
            {
                'title': 'Run Management',
                'description': 'Navigate to Run Management to start a new data acquisition run. Once a run is active, you can monitor it in real-time and make necessary adjustments.',
                'url': 'run_list'
            },
            {
                'title': 'Data Analysis',
                'description': 'Use the Data Analysis tools to deep-dive into your data. You can apply pre-defined or custom filters to get the insights you need.',
                'url': 'data_record_list'
            },
            {
                'title': 'Visualization',
                'description': 'The Visualization tools allow you to see your data in various formats. Interact with the data to gain deeper insights.',
                'url': None  # Add link if there's a URL pattern for visualization
            }
        ]

        context = {
            'functionalities': functionalities,
            'how_to_use': how_to_use
        }

        return render(request, 'analysis_home.html', context)
