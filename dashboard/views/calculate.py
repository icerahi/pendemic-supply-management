from django.views.generic import ListView
from django.views import View
from django.shortcuts import render

class CalculateView(View):
    def get(self,request,*args,**kwargs):
    
        return render(request,'calculate.html')