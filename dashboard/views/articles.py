from django.views.generic import ListView
from django.views import View
from django.shortcuts import render

class ArticleListView(View):
    def get(self,request,*args,**kwargs):
    
        return render(request,'articles.html')