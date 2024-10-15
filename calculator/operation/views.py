from django.shortcuts import render
from django.views.generic import View
# Create your views here.


class AdditionView(View):

    def get(sel,request,*args,**kwargs):

        return render(request,'addition.html')
