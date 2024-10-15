from django.shortcuts import render

from django.views.generic import View

#url:localhost:8000/morning/
#method:get


class HelloWorldView(View):

    def get(self,request,*args,**kwargs):

        return render(request,"hello_world.html")

class GoodMorningView(View):

    def get(self,request,*args,**kwargs):

        return render(request,"good_morning.html")



class SelfIntroView(View):
    def get(self,request,*args,**kwargs):
        data={"name":"arun","course":"cs","age":"23","gender":"male"}

        return render(request,"intro.html",data)

# localhost:8000/vehicle/

class VehicleDetailsView(View):
    def get(self,request,*args,**kwargs):
        data={"vehicel":"bmw","model":"2018","fuel":"petrol","reg_num":"387273"}

        return render(request,"vehichle_detail.html",data)