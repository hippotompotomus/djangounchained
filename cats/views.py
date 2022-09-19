from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import  CreateView, UpdateView,DeleteView

from .models import Cat, Breed
from .forms import BreedForm

class IndexView(LoginRequiredMixin, View):

    def get(self,request):
        ca = Cat.objects.all()
        bre = Breed.objects.all().count()
        context = {'cats_list':ca, 'breed_count': bre}
        return render(request, 'cats/cat_list.html', context)

class BreedView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'cats/breed_list.html', {'breed_list':Breed.objects.all()})

class BreedCreate(LoginRequiredMixin, View):
    template = 'cats/cat_form.html'
    success_url = reverse_lazy('cats:index')
    def get(self, request):
        form = BreedForm()
        return render(request, self.template, {'form':form})

    def post(self, request):
        form = BreedForm(request.POST)
        if not form.is_valid():
            return render(request, self.template, {'form':form})

        form.save()
        return redirect(self.success_url)



class BreedUpdate(LoginRequiredMixin, View):
    model = Breed
    template = 'cats/cat_form.html'
    success_url = reverse_lazy('cats:index')
    def get(self, request, pk):
        breed = get_object_or_404(self.model, pk=pk)
        form = BreedForm(instance=breed)
        return render(request, self.template, {'form':form})


    def post(self, request, pk):
        breed = get_object_or_404(self.model, pk=pk)
        form = BreedForm(request.POST, instance=breed)
        if not form.is_valid():
            return render(request, self.template, {'form':form})
        form.save()
        return redirect(self.success_url)

class BreedDelete(LoginRequiredMixin, View):
    model = Breed
    template = 'cats/breed_confirm_delete.html'
    success_url = reverse_lazy('cats:index')

    def get(self, request, pk):
        breed = get_object_or_404(self.model, pk=pk)
        return render(request, self.template, {'breed':breed})

    def post(self, request, pk):
        breed = get_object_or_404(self.model, pk=pk)
        breed.delete()
        return redirect(self.success_url)




class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:index')

class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:index')

class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:index')






