from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.
def landing_page(request):
    return render(request, 'core/landing-page.html')


def portfolio(request):
    return render(request, 'core/portfolio.html')


def testimonials(request):
    return render(request, 'core/testimonials.html')


def services(request):
    return render(request, 'core/services.html')


def lead_magnet(request):
    return render(request, 'core/lead-magnet.html')


def contact(request):
    return render(request, 'core/contact.html')


def about(request):
    return render(request, 'core/about.html')
