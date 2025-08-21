from django.shortcuts import render
from django.views.decorators.cache import cache_page

# @cache_page(60 * 60)  # Cache for 1 hour
def index(request):
    return render(request, 'core/index.html')


def cookies(request):
    return render(request, 'core/cookies.html')


def privacy(request):
    return render(request, 'core/privacy.html')


def terms(request):
    return render(request, 'core/terms.html')


def microservers(request):
    return render(request, 'core/microservers.html')
