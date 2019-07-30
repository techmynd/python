from django.shortcuts import render
# to send email
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
# from django.http import HttpResponse

# Create your views here.

# methods to process urls request from urls.py
# index is url name coming from url.py and it takes a request

from .models import Page


def index(request):
    # return HttpResponse('index page')

    #getPage = Page.objects.raw('SELECT * FROM pages_page WHERE id=1')
    pages = Page.objects.get(id=1)
    context = {
        'pages': pages
    }
    return render(request, 'pages/index.html', context)


def about(request):
    pages = Page.objects.get(id=2)
    context = {
        'pages': pages
    }
    return render(request, 'pages/about.html', context)


def contact(request):
    pages = Page.objects.get(id=3)
    context = {
        'pages': pages
    }
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
        return render(request, 'pages/emailsent.html', context)
    else:
        return render(request, 'pages/contact.html', context)
