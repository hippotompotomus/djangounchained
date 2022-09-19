from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import  DeleteView

from .models import Make, Auto
from .forms import MakeForm, AutoForm



# vjerojatno ovo mogu svesti na kraće
class MainView(LoginRequiredMixin, View):
    def get(self, request):
        au = Auto.objects.all()
        ma = Make.objects.all().count()
        context = {'auto_list' : au, 'make_count' : ma}
        return render(request, 'autos/auto_list.html', context)

class MakeView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'autos/make_list.html', {'make_list': Make.objects.all()})


class MakeCreate(LoginRequiredMixin, View):
    template = 'autos/make_form.html'
    success_url = reverse_lazy('autos:index')

    def get(self, request):
        form = MakeForm()
        context = {'form':form}
        return render(request, self.template, context)

    def post(self, request):
        form = MakeForm(request.POST)

        if not form.is_valid:
            context = {'form':form}
            return(request, self.template, context)

        form.save()
        return redirect(self.success_url)



class MakeUpdate(LoginRequiredMixin, View):
    model = Make
    template = 'autos/make_form.html'
    success_url = reverse_lazy('autos:index')

    def get(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        form = MakeForm(instance=make)
        context = {'form':form}
        return render(request, self.template, context)

    def post(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        form = MakeForm(request.POST, instance=make)
        if not form.is_valid(): #mogu ovde form.get() da skratim?
            context = {'form':form}
            return(request, self.template, context)

        form.save()
        return redirect(self.success_url)

class MakeDelete(LoginRequiredMixin, View):
    model = Make
    template = 'autos/confirm_make_delete.html'
    success_url = reverse_lazy('autos:index')

    def get(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        context = {'make':make }
        return render(request, self.template, context)

    def post(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        make.delete()
        return redirect(self.success_url)


class AutoCreate(LoginRequiredMixin, View):
    template_name = 'autos/auto_form.html'
    success_url = reverse_lazy('autos:index')
    def get(self,request):

        form = AutoForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = AutoForm(request.POST)
        if not form.is_valid():
            form = AutoForm()
            return render(request, self.template_name, {'form':form})



        form.save()
        return redirect(self.success_url)

class AutoUpdate(LoginRequiredMixin, View):
    model = Auto
    template = 'autos/auto_form.html'
    success_url = reverse_lazy('autos:index')

    def get(self, request, pk):
        auto = get_object_or_404(self.model, pk=pk)
        form = AutoForm(instance=auto)
        context = {'form':form}
        return render(request, self.template, context)

    def post(self, request, pk):
        auto = get_object_or_404(self.model, pk=pk)
        form = AutoForm(request.POST, instance=auto)
        if not form.is_valid(): #mogu ovde form.get() da skratim?
            context = {'form':form}
            return(request, self.template, context)

        form.save()
        return redirect(self.success_url)



class AutoDelete(LoginRequiredMixin, DeleteView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:index')




