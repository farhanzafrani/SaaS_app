from django.shortcuts import render


def home_page_view(request, *args, **kwargs):
    """
    A simple view that returns a 'Hello, World!' response.
    """
    content = {
        'page_title': 'SaaS',
        'request': request,
    }
    home_template = 'home.html'
    return render(request, home_template, content)

