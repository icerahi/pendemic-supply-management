from django.views.generic import ListView
from django.views import View
from django.shortcuts import render

class EquipmentListView(View):
    def get(self,request,*args,**kwargs):
    
        return render(request,'equipments.html')