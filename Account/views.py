from django.contrib import messages

# imports for logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth

# imports for login
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from .decoraters import unauthenticated_user

# imports for Signup
from .forms import SignupForm
from .tokens import account_activation_token


@unauthenticated_user
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            request.session["emailConfirm"] = form.cleaned_data.get("email")
            current_site = get_current_site(request)

            # For Email Confirmation
            mail_subject = "Activate your CVGenerator account."
            message = render_to_string(
                "Account/acc_active_email.html",
                {
                    "user": user,
                    "domain": current_site.domain,
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "token": account_activation_token.make_token(user),
                },
            )
            to_email = form.cleaned_data.get("email")
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return HttpResponseRedirect("/accounts/email-confirmation")
    else:
        form = SignupForm()
    return render(request, "Account/signup.html", {"form": form})


@method_decorator(unauthenticated_user, name="dispatch")
class LoginFormView(SuccessMessageMixin, LoginView):
    template_name = "Account/login.html"
    success_url = "list-of-cv"
    redirect_authenticated_user = False
    success_message = "You are successfully logged in."


# @unauthenticated_user
# def login(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get("username")
#             password = form.cleaned_data.get("password")

#             user = auth.authenticate(username=username, password=password)
#             print(user)
#             if user is not None:
#                 auth.login(request, user)
#                 return redirect("home")
#             else:
#                 messages.error(request, "Invalid Credentials")
#                 return redirect("login")
#     else:
#         form = LoginForm()
#     return render(request, "Account/login.html", {"form": form})


@unauthenticated_user
def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        auth.login(request, user, backend="django.contrib.auth.backends.ModelBackend")
        messages.success(request, f"Welcome {user.username}! You have successfully verified your account.")
        return redirect("home")
    else:
        messages.warning(request, "Activation link is invalid!")
        return redirect("home")


@unauthenticated_user
def email_confirmation(request):
    email = request.session["emailConfirm"]
    return render(request, "Account/email_confirmation.html", {"email": email})


@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, "You are successfully logged out")
    return HttpResponseRedirect(request.GET.get("next", "/"))
