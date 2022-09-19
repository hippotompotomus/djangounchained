from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

class OwnerListView(LoginRequiredMixin, ListView):
    x = 3

class OwnerCreateView(LoginRequiredMixin, CreateView):

    def form_valid(self, form):
        something = form.save(commit=False)
        something.owner = self.request.user
        something.save()
        form.save_m2m()
        return super(OwnerCreateView, self).form_valid(form)

class OwnerUpdateView(LoginRequiredMixin, UpdateView):

    def get_queryset(self):
        qs = super(OwnerUpdateView, self).get_queryset()
        return qs.filter(owner= self.request.user)

class OwnerDeleteView(LoginRequiredMixin, DeleteView):

    def get_queryet(self):
        qs = super(OwnerDeleteView, self).get_queryset()
        return qs.filter(owner=self.request.user)

