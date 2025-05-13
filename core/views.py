from django.shortcuts import render, redirect

from django.core.mail import send_mail
from django.conf import settings


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
    if request.method  == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        video_type = request.POST['video_type']
        message_content = request.POST['message_content']

        subject = f'You have received a message from TopResource.com from {name}'
        message = f'sender: {email}\nvideo type: {video_type}\nmessage: {message_content}'

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=True,
        )

        return redirect('landing_page')

    return render(request, 'core/contact.html')


def about(request):
    return render(request, 'core/about.html')
