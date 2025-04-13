from django.shortcuts import render, redirect
from .models import Team
from cars.models import Car
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages

def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    data = {
        'teams': teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }
    return render(request, 'pages/home.html', data)

def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', data)

def services(request):
    return render(request, 'pages/services.html')

def some_view(request):
    messages.success(request, 'Your action was successful!')
    messages.info(request, 'Here is some info.')
    messages.warning(request, 'This is a warning.')
    messages.error(request, 'Something went wrong.')
    return redirect('home')  # or wherever


def finance_calculator(request):
    emi = None
    if request.method == 'POST':
        try:
            price = float(request.POST['price'])
            down_payment = float(request.POST['down_payment'])
            interest_rate = float(request.POST['interest_rate']) / 100 / 12  # Monthly interest
            loan_term = int(request.POST['loan_term']) * 12  # Convert years to months
            loan_amount = price - down_payment

            if interest_rate > 0:
                emi = (loan_amount * interest_rate * (1 + interest_rate) ** loan_term) / ((1 + interest_rate) ** loan_term - 1)
            else:
                emi = loan_amount / loan_term
        except Exception as e:
            emi = "Invalid input: " + str(e)

    return render(request, 'pages/finance_calculator.html', {'emi': emi})


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        email_subject = 'You have a new message from CarDealer Website regarding ' + subject
        message_body = 'Name: ' + name + '. Email: ' + email + '. Phone: ' + phone + '. Message: ' + message

        admin_info = User.objects.filter(is_superuser=True).first()

        admin_email = admin_info.email
        send_mail(
            email_subject,
            message_body,
            'rathan.kumar049@gmail.com',
            [admin_email],
            fail_silently=False,
        )
        messages.success(request, 'Thank you for contacting us. We will get back to you shortly')
        return redirect('contact')

    return render(request, 'pages/contact.html')
