from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.conf import settings

from Notification.form import MailForm
from django.core.mail import send_mail
import os


def mail(request):
    if request.method == 'POST':

        form = MailForm(request.POST)
        if form.is_valid():

            send_mail(form.cleaned_data['subject_mail'],
                  'Here is where you make things right again!',
                  'seom@kdf.dfs',
                  [form.cleaned_data['to_mail']],
                  html_message=form.cleaned_data['content_mail']
                  )
            return redirect('search_donor')
                  
    else:
        form = MailForm()

    return render(request, 'mail1.html', {
        'form': form,
    })