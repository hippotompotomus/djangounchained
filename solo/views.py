from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.urls import reverse
from .models import Result
from .forms import CalculateForm

# Create your views here.
class MainView(LoginRequiredMixin, View):

	def get(self, request):
		try:
			result = Result.objects.all().order_by('-created_at')[0]
		except:
			result = None
		context = {'result':result}
		context['form'] = CalculateForm()
		return render(request, 'solo/main.html', context)

	def post(self, request):

		result = Result(result = str(request.POST['field1']).upper() + str(request.POST['field2']).upper())
		result.save()


		return redirect(reverse('solo:main'))


