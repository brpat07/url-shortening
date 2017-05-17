"""urlshort URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from goshort.views import goshort_redirect_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # simply add view for the function based view
    url(r'^a/(?P<shorturl>[\w-]+){7,15}$',goshort_redirect_view),
    # here shorturlcode will be whatever is after a/ in url address bar
    # suppose url is entered "localhost:8000/a/xyz" then
    # shorturlcode will be "xyz"

    # need to call view with as_view() method for the class based view
    # url(r'^b/(?P<shorturl>[\w-]+)/$',goshortCBview.as_view()),

]
