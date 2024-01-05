from core.forms import ContactForm
from django.shortcuts import render, redirect, HttpResponse
from django.core.mail import EmailMessage
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'core/index.html')


def about(request):
    return render(request, 'core/about.html')


# def contact(request):
#     return render(request, 'core/contact.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            message = form.cleaned_data['message']
            EmailMessage(
                'Contact Form Submission from{}'.format(email, name),

                message,
                'form-response@example.com',
                ['test.mailtrap123@gmail.com'],
                [],
                reply_to=[email]

            ).send()
            return redirect('/')


    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})


def success(request):
    return HttpResponse('success')


def login_admin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in")
            return redirect('dashboard')
        else:
            messages.success(request, "Error!!")
            return redirect('/')

    else:

        return render(request, 'core/login.html')


def logout_admin(request):
    pass


def dashboard(request):
    return render(request, 'core/dashboard.html')
