# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

def homepage(request, template=None): # Unpacking do dict
    return render_to_response(template, RequestContext(request))