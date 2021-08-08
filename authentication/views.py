from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse
from .forms import LoginForm, SignUpForm
from django.contrib.auth.decorators import login_required


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})


@login_required(login_url="/login/")
def get_users(request):
    users_data = User.objects.all()
    return render(request, "users.html", {'users': users_data})


@login_required(login_url="/login/")
def add_user(request):
    return render(request, "accounts/add-edit-user.html")


@login_required(login_url="/login/")
def save_user(request):
    if request.method == 'POST':
        if User.objects.filter(email=request.POST['email']).exists():
            return render(request, "accounts/add-edit-user.html", {"msg": "Email already exists", "error": True})
        else:
            user = User.objects.create(
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
                username=request.POST['username']
            )
            user.save()
            return redirect('users')


@login_required(login_url="/login/")
def edit_user(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, "accounts/add-edit-user.html", {'user': user})


@login_required(login_url="/login/")
def update_user(request, user_id):
    if request.method == 'POST':
        user = User.objects.filter(id=user_id)
        user.update(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            username=request.POST['username']
        )
        return redirect('users')


@login_required(login_url="/login/")
def delete_user(request, user_id):
    User.objects.filter(id=user_id).delete()
    return redirect('users')
