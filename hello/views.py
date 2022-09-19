
from django.http import HttpResponse

# Create your views here.

def assignment(request):
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    if num_visits > 4: del(request.session['num_visits'])
    resp = HttpResponse('b14306cd view count=' +str(num_visits))
    resp.set_cookie('dj4e_cookie', 'b14306cd', max_age=1000)
    return resp
