from django.views import View
from django.shortcuts import render
from core.models import TeamMember
from django.utils import timezone

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

class AboutView(View):
    def get(self, request):
        # get the people in the about page
        people = TeamMember.objects.all()

        return render(request, 'about.html', {'people': people})

class PrivacyPolicyView(View):
    def get(self, request):
        return render(request, 'privacy.html')