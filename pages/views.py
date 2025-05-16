from django.shortcuts import render, redirect

from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def landing_page(request):
    return render(request, 'pages/landing-page.html')


# def testimonials(request):
#     return render(request, 'pages/testimonials.html')


def services(request):
    return render(request, 'pages/services.html')


# def lead_magnet(request):
#     return render(request, 'pages/lead-magnet.html')


def contact(request):
    if request.method  == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        video_type = request.POST['video_type']
        message_content = request.POST['message_content']

        subject = f'You have received a message from TopResource.com from {name}'
        message = f'This is a test email to demostrate the email capabilities of the website. You can literally write any mail you want and send it. For example I am Yusuf. I went to the market. Bla, bla bla.\nsender: {email}\nvideo type: {video_type}\nmessage: {message_content}'
        fail_silently = True

        if settings.DEBUG:
            fail_silently = False

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=fail_silently,
        )

        return redirect('landing_page')

    return render(request, 'pages/contact.html')


# def about(request):
#     return render(request, 'pages/about.html')
