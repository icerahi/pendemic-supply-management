from django.db import models
from django.views.generic import CreateView,ListView
from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from stocks.models import Request

class ReqeustListCreateView(LoginRequiredMixin,ListView):
    login_url ='login'
    template_name='requests.html'
    queryset = Request.objects.all()
        
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['object_list']=Request.objects.filter(user=self.request.user)
        return context