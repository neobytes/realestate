from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class Property(models.Model):
    title = models.CharField(max_length=128, verbose_name=_('Title'))
    slug = models.SlugField(max_length=100, unique=True, blank=False, verbose_name=_('Slug'))
    description = models.TextField(verbose_name=_('Description'), null=True, blank=True)
    price = models.PositiveIntegerField(_('Price'), default=0, null=True, blank=True)
    available = models.BooleanField(_('Active'), default=False)

    # physical attributes of a property
    baths = models.PositiveIntegerField(_('Bathrooms'), default=0, null=True, blank=True)
    rooms = models.PositiveIntegerField(_('Rooms'), default=0, null=True, blank=True)
    parking = models.CharField(max_length=128, verbose_name=_('Parking'))

    #NOTE: 0 is for ground floor
    floor = models.PositiveIntegerField(_('Floor'), default=0, null=True, blank=True)

    # area of property in square meters
    area = models.PositiveIntegerField(_('Area)'), default=0, null=True, blank=True)

    owner = models.ForeignKey(User)

    # time stamps !
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))
    last_modified = models.DateTimeField(auto_now=True, verbose_name=_('Last Modified'))
