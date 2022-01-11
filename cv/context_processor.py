from django.contrib.auth.models import User

from cv.models import CV


def number_of_users_cvs(request):
    users = User.objects.all()
    cvs = CV.objects.all()

    skills = []
    for i in cvs:
        for j in i.skills:
            skills.append(j.lower())

    my_dict = {i: skills.count(i) for i in skills}

    return {
        "no_of_users": len(users),
        "no_of_cvs": len(cvs),
        "chart_keys": list(my_dict.keys()),
        "chart_values": list(my_dict.values()),
    }
