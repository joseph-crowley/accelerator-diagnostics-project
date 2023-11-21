from django.views import View
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator
from django.db.models import Q

from analysis.models import DataRecord
from analysis.forms import DataFilterForm

@method_decorator(login_required, name='dispatch')
class DataRecordListView(View):
    def get(self, request):
        filter_form = DataFilterForm(request.GET)
        data_records = DataRecord.objects.all().order_by('-timestamp')

        if filter_form.is_valid():
            data = filter_form.cleaned_data
            filters = Q()

            if data['start_date']:
                filters &= Q(timestamp__gte=data['start_date'])
            if data['end_date']:
                filters &= Q(timestamp__lte=data['end_date'])
            if data['run']:
                filters &= Q(run=data['run'])
            if data['group_id']:
                filters &= Q(run__group_id=data['group_id'])
            if data['dirpi_configurations']:
                filters &= Q(run__dirpi_configurations__in=data['dirpi_configurations'])
            
            data_records = data_records.filter(filters)

        paginator = Paginator(data_records, 25)  # Show 25 records per page

        page = request.GET.get('page')
        records = paginator.get_page(page)

        return render(request, 'data_analysis.html', {'data_records': records, 'filter_form': filter_form})


@method_decorator(login_required, name='dispatch')
class DataRecordDetailView(View):
    def get(self, request, pk):
        data_record = get_object_or_404(DataRecord, pk=pk)
        return render(request, 'data_record_detail.html', {'data_record': data_record})
