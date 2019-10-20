from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import People, Metadata #Paper, Product
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from taggit.models import Tag
#from . import forms
from .filters import MetadataFilter as MetaFilter

def home(request): # going to have to include the search parameters here as a form
    meta_list = Metadata.objects.all()
    meta_filter = MetaFilter(request.GET, queryset=meta_list)
#    meta_filter_qs = MetaFilter(request.GET, queryset=meta_list).qs
    
    paginator = Paginator(meta_filter.qs, 3)
    page = request.GET.get('page')
    try:
        response = paginator.page(page)
    except PageNotAnInteger:
        response = paginator.page(1)
    except EmptyPage:
        response = paginator.page(paginator.num_pages)
        
    return render(request, 'search/search_home.html',{'filter': meta_filter, 'response': response})


def profile(request):
    return render(request,'search/user_profile.html')

def search_list(request,tag_slug=None, query=None):
    object_list = Metadata.objects.all().order_by('date')
    query = request.GET.get("q")
    if query:
        object_list = object_list.filter(Q(title__icontains=query) | Q(body__icontains=query)).distinct()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])
    paginator = Paginator(object_list,9) # 9 blogs per page
    page = request.GET.get('page')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        images = paginator.page(1)
    except EmptyPage:
        # If the page is out of range deliver last page of results
        images = paginator.page(paginator.num_pages)
    return render(request,'search/search_list.html', {'page':page,'images':images,'tag':tag,'query':query})
    
def people_list(request):
    peoples = People.objects.all().order_by('date')
    return render(request,'search/people_list.html', {'peoples':peoples})


def people_detail(request, slug):
    people = People.objects.get(slug=slug)
    return render(request, 'search/people_detail.html',{'people':people})
    return HttpResponse(slug)

def mission(request):
    return render(request,'search/search_mission.html')

#    return render(request,'search/misson_list.html')
    
def contact(request):
    return render(request,'search/search_contact.html')

def detail(request, slug):
    metadata = Metadata.objects.get(slug=slug)
    return render(request, 'search/search_detail.html',{'metadata':metadata})
    return HttpResponse(slug)

