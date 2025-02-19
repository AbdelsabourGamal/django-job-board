from ast import In
from django.conf import settings
from django.shortcuts import render
from .models import Info
from django.core.mail import send_mail

# Create your views here.
def contact(request):
    contact = Info.objects.get(id=1)

    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
        print(subject)
        send_mail(
        subject,
        message,
        email,
        [settings.EMAIL_HOST_USER],
        )
                
    context = {'contact':contact}

    return render(request,'contact/contact.html',context) 