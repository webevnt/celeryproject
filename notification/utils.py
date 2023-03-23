from rest_framework.views import exception_handler
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from datetime import date
import os
from .models import *


class SendEmail():
    def send_notification_email(self, email):
        user = User.objects.filter(email=email).first()
        sale_order = SaleOrder.objects.filter(user=user).first()
        subscribers = Subscribers.objects.filter(sale_order=sale_order)
        if subscribers.exists():
            subscriber = subscribers.first()
        else:
            return False
        
        notification_txns_data = {'user':user,'subscriber':subscriber,'name':f'Payment Not. {user.first_name}'}
        
        mail_data = {'user':user,'country':subscriber.country.name,'store':subscriber.store.name,'item':sale_order.name,'amount':sale_order.amount}
    
        try:
            
            # render template mail.txt
            subject = "Payment Remainder"
            body = render_to_string('mail.html', context={
                'action_url': "http://",
                'meta': mail_data,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            })

            # set mail to email content with subject, body ,sender and recepient
            # with html content type
            mail = EmailMessage(subject, body, "admin@vaultedge.com", to=[email])
            mail.content_subtype = 'html'
            # send email
            mail.send()
            notification_txns_data.update({'sent':True})
            NotificationTransaction.objects.create(**notification_txns_data)
            sale_order.paid = True
            sale_order.save()
            return True
        except Exception as mail_error:
            print(mail_error)
            NotificationTransaction.objects.create(**notification_txns_data)
            return False