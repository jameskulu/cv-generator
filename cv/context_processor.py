from django.contrib.auth.models import User

from cv.models import CV


def number_of_users_cvs(request):
    users = User.objects.all()
    cvs = CV.objects.all()
    return {
        'no_of_users': len(users),
        'no_of_cvs': len(cvs)
    }
