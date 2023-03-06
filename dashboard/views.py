from django.shortcuts import render
from django.views.generic import TemplateView


#dashboard
class DashboardListView(TemplateView):
    
    template_name = 'dashboard/index.html'


