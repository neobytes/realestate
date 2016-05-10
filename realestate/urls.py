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

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'property.views.home', name='home'),
	url(r'^home', 'property.views.home', name='home'),

    # properties
    url(r'property/(\d+)$', 'property.views.property', name='property'),
    url(r'^save_property/$', 'property.views.save_property', name='save_property'),	
	url(r'^add_property/$', 'property.views.add_property', name='add_property'),
	url(r'^buying', 'property.views.buying', name='buying'),
	url(r'^selling', 'property.views.selling', name='selling'),	
	url(r'^mortages', 'property.views.mortages', name='mortages'),	
	url(r'^homeforsale', 'property.views.homeforsale', name='homeforsale'),
	url(r'^fore', 'property.views.fore', name='fore'),	
	url(r'^lotsandland', 'property.views.lotsandland', name='lotsandland'),	
	url(r'^freehomeplans', 'property.views.freehomeplans', name='freehomeplans'),	
	url(r'^agents', 'property.views.agents', name='agents'),
	url(r'^contact', 'property.views.contact', name='contact'),
	url(r'^about', 'property.views.about', name='about'),
	url(r'^moving', 'property.views.moving', name='moving'),
	url(r'^rental', 'property.views.rental', name='rental'),			
]
