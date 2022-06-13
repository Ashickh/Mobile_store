from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import View
# from mobiles.forms import LoginForm
# from mobiles.forms import RegForm
from mobiles.forms import MobileForm
from django.contrib import messages


class HomeView(View):

    def get(self,request):
        return render(request,'home.html')


class AddMobileView(View):
    form_class=MobileForm
    temp_name="add-mob.html"
    def get(self,request):
        form=self.form_class()
        return render(request,self.temp_name,{'form':form})
    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            print(form.cleaned_data.get("mob_id"))
            print (form.cleaned_data.get ("mob_name"))
            print (form.cleaned_data.get ("brand"))
            print (form.cleaned_data.get ("price"))
            print (form.cleaned_data.get ("color"))
            print (form.cleaned_data.get ("memory"))
            messages.success(request,'MOBILE ADDED SUCCESSFULLY')
            return redirect('add-mob')
        else:
            messages.error(request,'ADDING FAILED')
            return render(request,self.temp_name,{'form':form})




# Create your views here.
