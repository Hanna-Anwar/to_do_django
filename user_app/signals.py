from django.db.models.signals import post_save

from django.dispatch import receiver

from  user_app.models import User

from django.core.mail import send_mail


@receiver(post_save,sender=User)
def send_reg_mail(sender,instance,created,**kwargs):

    if created:

        subject = "welcoming message"

        message = "Welcome to Todo"

        from_email= "hannaanwar469@gmail.com"

        recipient_list = [instance.email]

        send_mail(subject=subject,message=message,from_email=from_email,recipient_list=recipient_list,fail_silently=True)

        print("mail sended")