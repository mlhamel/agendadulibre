from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.models import User
from django.conf import settings

def mail_moderators(title, message):
    moderators = User.objects.filter(is_staff=True).filter(is_active=True)
    to_emails = [x.get('email') for x in moderators.values('email')]
    from_email = settings.FROM_EMAIL
    
    if title and message and from_email:
        try:
            send_mail(title, message, from_email, to_emails)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return True
    return False
