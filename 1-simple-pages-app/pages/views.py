from django.shortcuts import render
# to send email
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
# from django.http import HttpResponse

# Create your views here.

# methods to process urls request from urls.py
# index is url name coming from url.py and it takes a request


def index(request):
    # return HttpResponse('index page')
    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    if request.method == 'POST':
        sender_name = request.POST['sender_full_name']
        sender_email = request.POST['sender_email_address']
        sender_message = request.POST['email_message']
        full_message = sender_name + " with email address " + sender_email + \
            " sent you following message " + sender_message
        send_mail('Inquiry from Contact Form',
                  full_message,
                  settings.EMAIL_HOST_USER,
                  ['receivingemailaddress@server.com'],
                  fail_silently=False)
        return render(request, 'pages/emailsent.html')
    else:
        return render(request, 'pages/contact.html')
