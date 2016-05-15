# coding=utf-8
__author__ = 'xiaobo'

from django.contrib.auth.decorators import login_required

def index(request):
    from django.shortcuts import render_to_response
    from django.template import RequestContext
    return render_to_response("index.html", locals(), context_instance=RequestContext(request))
