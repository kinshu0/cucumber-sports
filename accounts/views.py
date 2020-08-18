from django.shortcuts import render

# Create your views here.
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm

from .forms import CustomUserCreationForm

from accounts import helpers
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings

from django.shortcuts import redirect, get_object_or_404, reverse, Http404

from .models import Author

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            # send email verification now
            activation_key = helpers.generate_activation_key(username=request.POST['username'])

            subject = "TheGreatDjangoBlog Account Verification"

            message = '''\n
Please visit the following link to verify your account \n\n{0}://{1}/cadmin/activate/account/?key={2}
                        '''.format(request.scheme, request.get_host(), activation_key)            

            error = False

            try:
                send_mail(subject, message, settings.SERVER_EMAIL, [request.POST['email']])
                messages.add_message(request, messages.INFO, 'Account created! Click on the link sent to your email to activate the account')

            except:
                error = True
                messages.add_message(request, messages.INFO, 'Unable to send email verification. Please try again')

            if not error:
                u = User.objects.create_user(
                        request.POST['username'],
                        request.POST['email'],
                        request.POST['password1'],
                        is_active = 0
                )

                author = Author()
                author.activation_key = activation_key
                author.user = u
                author.save()

            return redirect('register')


    else:
        f = CustomUserCreationForm()

    return render(request, 'cadmin/register.html', {'form': f})

def activate_account(request):
    key = request.GET['key']
    if not key:
        raise Http404()

    r = get_object_or_404(Author, activation_key=key, email_validated=False)
    r.user.is_active = True
    r.user.save()
    r.email_validated = True
    r.save()

    return render(request, 'cadmin/activated.html')