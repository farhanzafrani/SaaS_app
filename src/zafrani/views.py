from django.shortcuts import render
from visits.models import PageVisit


def home_page_view(request, *args, **kwargs):
    """
    A simple view that returns a 'Hello, World!' response.
    """
    qs = PageVisit.objects.all()
    path_qs = PageVisit.objects.filter(path=request.path)

    content = {
        'page_title': 'SaaS',
        'request': request,
        'qs_counts': qs.count(),
        'path_qs_count': path_qs.count(),
    }
    PageVisit.objects.create(path=request.path)
    home_template = 'home.html'
    return render(request, home_template, content)

def about_page_view(request, *args, **kwargs):
    """
    A simple view that returns an 'About' response.
    """
    content = {
        'page_title': 'About',
        'request': request,
    }
    about_template = 'about.html'
    return render(request, about_template, content)

