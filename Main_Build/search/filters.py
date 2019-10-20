# -*- coding: utf-8 -*-
#from django.contrib.auth.models import User, Group
from .models import Metadata
import django_filters

class MetadataFilter(django_filters.FilterSet):
#    first_name = django_filters.CharFilter(lookup_expr='icontains')
#    x_coord__gt = django_filters.NumberFilter(name='x_coord__low', lookup_expr='x_coord__gt')
#    x_coord__lt = django_filters.NumberFilter(name='x_coord__up', lookup_expr='x_coord__lt') 
    class Meta:
        model = Metadata
        fields = ['year' ,'month', 'day','x_coord', 'y_coord', 'z_coord', ]
        
        