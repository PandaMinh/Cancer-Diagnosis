# from django.db.models.signals import post_save
# from django.conf import settings
# from django.dispatch import receiver
# from django.core.mail import send_mail
# from django.utils import timezone
# from myweb.models import OtpToken
 
 
# @receiver(post_save, sender=settings.AUTH_USER_MODEL) 
# def create_token(sender, instance, created, **kwargs):
#     if created:
#         if instance.is_superuser:
#             pass
        
#         else:
#             OtpToken.objects.create(user=instance, otp_expires_at=timezone.now() + timezone.timedelta(minutes=5))
#             instance.is_active=False 
#             instance.save()
        
        
#         # email credentials
#         otp = OtpToken.objects.filter(user=instance).last()
       
       
#         subject="Email Verification"
#         message = f"""
#                                 Hi {instance.username}, here is your OTP {otp.otp_code} 
#                                 it expires in 5 minute, use the url below to redirect back to the website
#                                 http://127.0.0.1:8000/verify-email/{instance.username}
                                
#                                 """
#         sender = "clintonmatics@gmail.com"
#         receiver = [instance.email, ]
       
        
        
#         # send email
#         send_mail(
#                 subject,
#                 message,
#                 sender,
#                 receiver,
#                 fail_silently=False,
#             )
  
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.utils import timezone
from django.conf import settings
from myweb.models import OtpToken


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_token(sender, instance, created, **kwargs):
    if created:
        if instance.is_superuser:
            return
        
        # Create OTP token
        otp = OtpToken.objects.create(
            user=instance, 
            otp_expires_at=timezone.now() + timezone.timedelta(minutes=5)
        )
        
        # Deactivate the user until OTP is verified
        instance.is_active = False
        instance.save()
        
        # Email credentials
        subject = "Email Verification"
        message = f"""
            Hi {instance.username}, here is your OTP: {otp.otp_code}.
            It expires in 5 minutes. Use the URL below to verify your email:
            http://127.0.0.1:8000/verify-email/{instance.username}
        """
        sender = "clintonmatics@gmail.com"
        receiver = [instance.email]
        
        # Send email
        send_mail(
            subject,
            message,
            sender,
            receiver,
            fail_silently=False,
        )
