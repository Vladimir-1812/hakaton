from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from hakaton_app.models import *
from hakaton_app.forms import LoginForm, RegistrationForm, ProblemForm

import datetime

def get_base_context(request, pagename):
    return {
        'pagename': pagename,
        'loginform': LoginForm(),
        'user': request.user,
    }

def index(request):
    context = get_base_context(request, "Проблемы города Санкт-Петербург")
    context["problems_list"] = Problem.objects.order_by("date").reverse()
    return render(request, "pages/index.html", context)

def smap(request):
    context = get_base_context(request, "Карта")
    id = int(request.GET.get("id"))
    try:
        prob = Problem.objects.get(id=id)
    except BaseException:
        return render(request, "pages/smap.html", context)
    context["prob"] = prob
    return render(request, "pages/smap.html", context)

def mmap(request):
    context = get_base_context(request, "Карта")
    if request.method == "POST":
        if request.POST["set"] == "all":
            context["prob_list"] = Problem.objects.all()
        elif request.POST["set"] == "user":
            context["prob_list"] = Problem.objects.filter(author_id=request.user.id)
        else:
            context["prob_list"] = []
    print(len(context["prob_list"]))
    return render(request, "pages/mmap.html", context)

def login_check_page(request):
    if request.method == 'POST':
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            username = loginform.data['username']
            password = loginform.data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, "Авторизация успешна")
            else:
                messages.add_message(request, messages.ERROR, "Неправильный логин или пароль")
        else:
            messages.add_message(request, messages.ERROR, "Некорректные данные в форме авторизации")
    return redirect('index')

def logout_page(request):
    logout(request)
    messages.add_message(request, messages.INFO, "Вы успешно вышли из аккаунта")
    return redirect('index')

def registration_page(request):
    context = get_base_context(request, "Регистрация")
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = User()
            new_user.email = user_form.data['emale']
            new_user.username = user_form.data['username']
            new_user.first_name = user_form.data['first_name']
            new_user.last_name = user_form.data['last_name']
            new_user.set_password(user_form.data['password'])
            new_user.save()
            messages.add_message(request, messages.INFO, "Регистрация прошла успешно")
            return redirect("index")
        else:
            if user_form.data["password"] != user_form.data["password2"]:
                messages.add_message(request, messages.ERROR, "Пароли не совпадают")

    else:
        user_form = RegistrationForm()
    context['user_form'] = user_form
    return render(request, "pages/registration.html", context)


@login_required
def user_problems(request):
    context = get_base_context(request, "Мои проблемы")
    context["problems_list"] = Problem.objects.filter(author_id=request.user.id)
    return render(request, "pages/sub_prob.html", context)


@login_required
def create_problem(request):
    context = get_base_context(request, "Добавить проблему")
    if request.method == 'POST':
        problem_form = ProblemForm(request.POST)
        if problem_form.is_valid():
            record = Problem()
            record.lat = problem_form.data["lat"]
            record.lng = problem_form.data["lng"]
            record.type = int(problem_form.data["problem_type"])
            record.date = datetime.datetime.today()
            record.description = problem_form.data["description"]
            record.votes_neg = 0
            record.votes_pos = 0
            record.author_id = request.user.id
            record.save()
            messages.add_message(request, messages.INFO, "Проблема успешно создана")
            return redirect("index")
    else:
        problem_form = ProblemForm()
    context['problem_form'] = problem_form
    context["prob_list"] = Problem.objects.all()
    return render(request, "pages/add_prob.html", context)

def login_page(request):
    context = get_base_context(request, "")
    return render(request, "pages/login_page.html", context)