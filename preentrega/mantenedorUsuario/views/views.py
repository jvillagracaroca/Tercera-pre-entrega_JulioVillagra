# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.shortcuts import render
from django.template import Context, Template
from django.http import HttpResponse

def index(request):

    path = os.path.join(os.path.dirname(__file__), '../templates/index.html')
    with open(path, 'r') as file:
        content = file.read()
    template = Template(content)
    context = Context()
    rendered_html = template.render(context)
    
    return HttpResponse(rendered_html)