from django.shortcuts import render
from django.views.decorators.cache import cache_page

from .models import AIService, Project, Service


# @cache_page(60 * 60)  # Cache for 1 hour
def index(request):
    context = {
        'services': Service.objects.filter(is_active=True),
        'ai_services': AIService.objects.filter(is_active=True),
        'projects': Project.objects.filter(is_active=True),
    }
    return render(request, 'core/index.html', context)


def cookies(request):
    return render(request, 'core/cookies.html')


def privacy(request):
    return render(request, 'core/privacy.html')


def terms(request):
    return render(request, 'core/terms.html')


def microservers(request):
    return render(request, 'core/microservers.html')


def digital_signage(request):
    return render(request, 'core/digital_signage.html')
