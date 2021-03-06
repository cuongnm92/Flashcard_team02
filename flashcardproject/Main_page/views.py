﻿# Create your views here.
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login , logout
from django.template.context import RequestContext


def main_page(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/flashcard")
    return render_to_response('mainpage/index.html')

def login_page(request):
    if request.user.is_authenticated():
        HttpResponseRedirect('/flashcard')
    error = 0
    redirect_to = request.REQUEST.get('next', '')
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(redirect_to)
            else:
                error = 1
        else:
            error = 1
        variables = RequestContext(request, {'error': error})
        return render_to_response('mainpage/login.html', variables)
    variables = RequestContext(request, {'error': error})
    return render_to_response('mainpage/login.html', variables)

@login_required(login_url='/login/')
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')