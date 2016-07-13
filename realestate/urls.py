"""realestate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from property import views

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^home', views.home, name='home'),

    # properties
    url(r'property/(\d+)$', views.property, name='property'),
    url(r'^add_property/$', views.add_property, name='add_property'),
    url(r'^buying', views.buying, name='buying'),
    url(r'^selling', views.selling, name='selling'),	
    url(r'^mortages', views.mortages, name='mortages'),	
    url(r'^homeforsale', views.homeforsale, name='homeforsale'),
    url(r'^fore', views.fore, name='fore'),	
    url(r'^lotsandland', views.lotsandland, name='lotsandland'),	
    url(r'^freehomeplans', views.freehomeplans, name='freehomeplans'),	
    url(r'^agents', views.agents, name='agents'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^about', views.about, name='about'),
    url(r'^moving', views.moving, name='moving'),
    url(r'^rental', views.rental, name='rental'),	
    url(r'^save_property', views.save_property, name='save_property'),
    url(r'^main', views.main, name='main'),			
]
