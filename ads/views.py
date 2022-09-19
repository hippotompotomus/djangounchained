from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
from django.views import View
from django.db.models import Q
from django.conf import settings

from .forms import CreateForm, CommentForm
from .owner import OwnerDeleteView, OwnerListView
from .models import Ad, Comment, Favorite
# Create your views here.

class AdListView(ListView):
    model = Ad
    template_name = 'ads/ad_list.html' 

    def get(self, request):

        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0


        ad_list = Ad.objects.all()
        favorites = []
        tag_dict = {}
        tags = []
        search_query = request.GET.get('search', False)
        if search_query:
            query = Q(title__icontains=search_query)
            query.add(Q(text__icontains=search_query), Q.OR)
            query.add(Q(tags__slug__in=[search_query]), Q.OR)
            ad_list=Ad.objects.filter(query).distinct().select_related().order_by('-updated_at')

        try:
            rows = self.request.user.user_favorited.values('id')
            favorites = [row['id'] for row in rows]
        except: favorites = []

        context={'ad_list':ad_list, 'favorites':favorites, 'search': search_query, 'installed': settings.INSTALLED_APPS,'islocal': islocal}
        return render(request, self.template_name, context)



class AdDetailView(DetailView):
    model = Ad
    template_name = 'ads/ad_detail.html'
    def get(self, request, pk):

        ad = Ad.objects.get(id=pk)
        comments = Comment.objects.filter(ad=ad).order_by('-updated_at')
        comment_form = CommentForm()
        tags = ad.tags.all()
        context = {'ad':ad, 'comments' : comments, 'comment_form':comment_form, 'tags':tags}
        return render(request, self.template_name, context)

def stream_file(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    response = HttpResponse()
    response['Content-Type'] = ad.content_type
    response['Content-Length'] = len(ad.picture)
    response.write(ad.picture)
    return response



class AdCreateView(LoginRequiredMixin, CreateView):
    model = Ad

    success_url = reverse_lazy('ads:index')
    template_name = 'ads/ad_form.html'

    def get(self, request):
        form = CreateForm()
        context = {'form':form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = CreateForm(request.POST, request.FILES or None)
        if not form.is_valid():
            return render(request, self.template_name, {'form':form})

        bugfix = form.save(commit=False)#nisam ziher zakej je ovo potrebno


        bugfix.owner = self.request.user
        bugfix.save()
        form.save_m2m()
        return redirect(self.success_url)



class AdUpdateView(LoginRequiredMixin, UpdateView):
    model = Ad
    fields = ['title', 'price', 'text', 'picture']
    success_url = reverse_lazy('ads:index')
    template_name = 'ads/ad_form.html'

    def get(self, request, pk):
        a = get_object_or_404(Ad, pk=pk, owner=self.request.user)
        form = CreateForm(instance=a)
        context = {'form':form, 'ad':a}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        a = get_object_or_404(Ad, pk=pk, owner=self.request.user)
        form = CreateForm(request.POST, request.FILES or None, instance = a)

        if not form.is_valid():
            context = {'form':form}
            return render(request, self.template_name, context)

        a = form.save(commit=False)
        a.save()
        form.save_m2m() 
        return redirect(self.success_url)



class AdDeleteView(OwnerDeleteView):
    model = Ad

class CommentCreateView(LoginRequiredMixin, View):


    def post(self, request, pk):
        a = get_object_or_404(Ad, id=pk)
        comment = Comment(text=request.POST['comment'], owner = request.user, ad= a)
        comment.save()
        return redirect(reverse('ads:ad_detail', args=[pk]))


class CommentDeleteView(OwnerDeleteView):
    model = Comment
    template_name = 'ads/comment_confirm_delete.html'

    def get_success_url(self):
        ad = self.object.ad
        return reverse('ads:ad_detail', args=[ad.id])

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.utils import IntegrityError

@method_decorator(csrf_exempt, name='dispatch')
class AddFavoriteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        a = get_object_or_404(Ad, pk=pk)
        fav = Favorite(user = request.user, ad=a, id=pk)#bog zna zakej sam ne zada id
        try: 

            fav.save()
        except IntegrityError as e: pass 
        return HttpResponse()


@method_decorator(csrf_exempt, name='dispatch')
class DeleteFavoriteView(LoginRequiredMixin, View):
    def post(self,request,pk):
        a = get_object_or_404(Ad, pk=pk)
        
        try: 
            fav = Favorite(user = request.user, ad=a, id=pk).delete()
        except Favorite.DoesNotExist as e: pass
        return HttpResponse()
