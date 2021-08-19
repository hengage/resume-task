from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, redirect

from apps.resume.forms import ContactForm


def home(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            senders_email = form.cleaned_data['senders_email']

            try:
                send_mail(subject, message, senders_email, ['tunecarterkillz@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            messages.success(request, 'Than you for contacting me.')
            return redirect('home')
    return render(request, 'home.html', {'form':form})
