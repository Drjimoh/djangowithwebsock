from django.shortcuts import render
from django.utils.safestring import mark_safe
import json


'''def index(request):
    return render(request, 'websock/index.html',
                  {})'''

def index(request):
    return render(request, 'websock/index.html', {})