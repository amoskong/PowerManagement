from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from Switch.models import Switch

# Create your views here.

def getobj():
    try:
        s = Switch.objects.get()
    except Exception:
        s = Switch()
        s.save()
    return s

def getstate(request):
    s = getobj()
    return HttpResponse('Switch state is (%d)' % s.state)

def setstate(request):
    s = getobj()
    if request.GET.get('state', -1) > 0:
        s.state = int(request.GET.get('state'))
        s.save()
    return HttpResponse('Set switch state to (%d)' % s.state)
