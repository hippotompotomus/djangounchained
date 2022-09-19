from django.shortcuts import render
from django.views import View
from django.conf import settings

# Create your views here.

# This is a little complex because we need to detect when we are
# running in various configurations


class HomeView(View):
    x = 3
