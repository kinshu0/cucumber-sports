# Create your views here.
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm

from .forms import CustomUserCreationForm

from accounts import helpers
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings

from django.shortcuts import redirect, get_object_or_404, reverse, Http404, render

from .models import Profile, Registration

from django.template.loader import get_template


from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required

'''
Home Page
'''
def index(request):
    return render(request, 'index.html')


'''
Registration Page
'''
def register(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            # send email verification now
            activation_key = helpers.generate_activation_key(username=request.POST['username'])

            subject = "Cucumber Sports Account Verification"    
            verification_link = f'{request.scheme}://{request.get_host()}/activate/{activation_key}'

            message = (
                f'Hello {request.POST["first_name"]},\nPlease visit the following link to verify your account:\n'
                f'{verification_link}'
            )
            
            # message = get_template('verification_email.html').render({
            #     'verification_link': verification_link
            # })

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

                profile = Profile()
                profile.activation_key = activation_key
                profile.user = u

                profile.first_name = request.POST['first_name']
                profile.last_name = request.POST['last_name']

                profile.save()

            return redirect('register')


    else:
        f = CustomUserCreationForm()

    return render(request, 'accounts/register.html', {'form': f})


'''
Email verification
'''
def activate_account(request, activation_key):
    if not activation_key:
        raise Http404()

    r = get_object_or_404(Profile, activation_key=activation_key, email_validated=False)
    r.user.is_active = True
    r.user.save()
    r.email_validated = True
    r.save()

    return render(request, 'activated.html')


'''
Login Page
'''
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)

            u = Profile.objects.get(user=user)
            # u = CustomUser.objects.get(username=username)
            # btcBalance = getBtcBalance(u.btcKey)

            ## Set session variables    
            request.session['first_name'] = u.first_name
            # request.session['username'] = u.username
            # request.session['btcAddress'] = u.btcAddress
            # request.session['balance'] = btcBalance
            # request.session['apiKey'] = u.apiKey
            # request.session['conversionRate'] = getBtcPrice()
            # qrBinary = u.qrCodeBinary
            # request.session['qrCodeBinary'] = json.dumps(qrBinary.decode("utf-8"))

            # ## Find, update and payout games that are not up to date
            # oddsApiParse.findUpcomingGames()
            # oddsApiParse.checkForCompletedGames()
            # oddsApiParse.payoutCompletedGames()
            
            # return redirect('admin/')
            return redirect(request.POST.get('next'))
            # return redirect(request.POST.get('next', '/accounts/profile'))
        else:
            return render(request, 'accounts/login.html', {'message': 'Invalid Login'})

    else:
        return render(request, 'accounts/login.html')

@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    context = {
        'profile': profile,
        'registrations': Registration.objects.filter(profile=profile),
    }

    return render(request, 'accounts/profile.html', context)