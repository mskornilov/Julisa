from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate

# Create your views here.
def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password-confirm']
        email = request.POST['e-mail']
        if password != password_confirm:
            context = {'error': 'Пароли не совпадают'}
            return render(request, 'registration/register.html', context)
        else:
            username_exists = User.objects.filter(username=username)
            email_exists = User.objects.filter(email=email)
            if not username_exists and not email_exists:
                user = User.objects.create(username=username, email=email)
                user.set_password(password)
                user.save()
                message = 'Регистрация прошла успешно, \
                           теперь вы можете зайти под своим логином и паролем'
                messages.add_message(request, messages.INFO, message)
                return redirect('login')
            else:
                context = {'error': 'Пользователь с таким именем или \
                           электронной почтой уже существует'}
                return render(request, 'registration/register.html', context)
    else:
        return render(request, 'registration/register.html')


def profile_details(request):
    return render(request, 'account/profile_details.html')
