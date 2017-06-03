from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import ShortenURL

# Create your views here.
# function base view
# def goshort_redirect_view(request, shorturl=None, *args, **kwargs):
#     obj = get_object_or_404(ShortenURL, shorturl=shorturl)
#     return HttpResponseRedirect("http://"+obj.url)


# class base view
class goshortCBview(View):
    def get(self, request, shorturl=None, *args, **kwargs):
        obj = get_object_or_404(ShortenURL, shorturl=shorturl)
        return HttpResponseRedirect("http://"+obj.url)
