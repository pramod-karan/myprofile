from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Contact


from django.template.loader import render_to_string
from django.core.mail import EmailMessage

# Create your views here.
def contacts(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        contact=Contact(username=username,email=email,subject=subject,message=message)
        contact.save()
        mail_subject="Query submited sucessfully."
        message=render_to_string('contacts/contacts_email_recieve.html',{
        'username':username,
        'subject':subject,
        'message':message,
        })
        to_email=email
        send_email=EmailMessage(mail_subject,message,to=[to_email])
        send_email.send()
        return redirect('index')
    else:
        return HttpResponse("Get Method")
