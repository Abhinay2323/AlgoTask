from django.shortcuts import render
from userform.models import *

from datetime import datetime
from django.core.exceptions import ValidationError
from django.core.mail import EmailMessage, send_mail
from django.shortcuts import render_to_response


def home(request):
    return render(request,'form.html')


def formuser(request):

    name = request.POST.get('name')
    Email = request.POST.get('email')
    phone = request.POST.get('phone_number')
    dob = request.POST.get('date')
    dob = datetime.strptime(dob, '%Y-%m-%d')

    today = datetime.today()
    age = (today - dob).days/365
    age = (today - dob).days/365
    if age < 18:
        listu="Hello world"
        context = {"list":listu}
        return render(request,'error.html',context)

        
    ForLogin.objects.create(name=name, dob=dob, email=Email, phone_number=phone)
    list = ForLogin.objects.all()
    context = {"list":list}


#SENDING EMAIL
    subject = 'Confirmation mail for Login activity at ALGOFOCUS'
    message = 'Hi user,your details are successfuly registered at ALGOFOCUS.'
    toemail = Email
    email = EmailMessage(subject, message, to=[toemail])
    email.send()

    return render(request,'main.html', context)