from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from  NewEmailProject import settings
from django.core.mail import EmailMessage

# Create your views here.



def index(request):  
   send_mail(
    'That’s your subject',
    'That’s your message body',
    'from@yourdjangoapp.com',
    ['to@yourbestuser.com'],
    fail_silently=False,
)
   return HttpResponse('message sent!!!')





























# with get_connection(  
#         host=settings.EMAIL_HOST, 
#         port=settings.EMAIL_PORT,  
#         username=settings.EMAIL_HOST_USER, 
#         password=settings.EMAIL_HOST_PASSWORD, 
#         use_tls=settings.EMAIL_USE_TLS  
#        ) as connection:  
#            subject = request.POST.get("subject")  
#            email_from = settings.EMAIL_HOST_USER  
#            recipient_list = [request.POST.get("email"), ]  
#            message = request.POST.get("message")  
#            EmailMessage(subject, message, email_from, recipient_list, connection=connection).send() 