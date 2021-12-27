from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from first_app.models import UserInfo, Topic, WebPage, AccessRecord
from . import forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse


# Create your views here.

def index(request):
    dict = { 'django_var': 'Data from first app variable'}
    return render(request, 'first_app/index.html', context=dict)


def user_login(request):
    print('before post')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print('before auth')
        user = authenticate(request, username=username, password=password)
        print('authenticated')
        if user:
            print('loggin in')
            login(request, user)
            print('logged in')
            return render(request, 'first_app/index.html', {})
        else:
            return render(request, 'first_app/login_page.html',
                                    {'msg': 'login failed'})


    return render(request, 'first_app/login_page.html',
                                {'msg': ''})

@login_required
def user_logout(request):
    logout(request)
    return render(request, 'first_app/index.html', {})

def register_user(request):
    user_form = forms.UserForm()
    user_info_form = forms.UserInfoForm()

    if request.method == 'POST':
        user_form = forms.UserForm(request.POST)
        user_info_form = forms.UserInfoForm(request.POST, request.FILES)

        if user_form.is_valid() and user_info_form.is_valid():
            user_form.save()
            user = User.objects.get(username=user_form.cleaned_data['username'])
            user.set_password(user.password)
            user.save()

            if 'pic' in request.FILES:
                user_info = UserInfo(user=user,
                                    pic=user_info_form.cleaned_data['pic'])
                user_info.save()
                print('pic saved')
                return render(request, 'first_app/index.html',
                    {
                    'msg': 'Registered'
                    }
                )
            return render(request, 'first_app/index.html',
                {
                'msg': 'Pic not valid'
                }
            )
        else:
            return render(request, 'first_app/register.html',
                {
                'user_form': user_form,
                'user_info_form': user_info_form,
                'msg': 'Invalid credentials'
                }
            )
    return render(request, 'first_app/register.html',
        {
        'user_form': user_form,
        'user_info_form': user_info_form
        }
    )

def show_records(request):
    records = AccessRecord.objects.order_by('date')
    rec_dict = { 'records': records }
    return render(request, 'first_app/access_records.html', rec_dict)


def show_login(request):
    return render(request, 'first_app/login.html', {'form': forms.LoginForm})

def insert_webpage(request):
    web_form = forms.WebForm()

    if request.method == 'POST':
        web_form = forms.WebForm(request.POST)

        if web_form.is_valid():
            web_form.save()
            return render(
                request,
                'first_app/web_form.html',
                {
                'form': web_form,
                'msg': 'Data Saved'
                }
            )
        else:
            return render(
                request,
                'first_app/web_form.html',
                {
                'form': web_form,
                'msg': 'Data not Valid'
                }
            )


    return render(
        request,
        'first_app/web_form.html',
        {
        'form': web_form,
        'msg': ''
        }
    )

def validate_login(request):
    login_form = forms.LoginForm()

    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)

        if login_form.is_valid():
            password_1 = login_form.cleaned_data['password']
            password_2 = login_form.cleaned_data['reenter_password']
            print(password_1 + '    ' + password_2)
            if password_1 != password_2:
                return render(request,
                             'first_app/login.html',
                             {
                             'msg': 'Password mismatch',
                             'form': forms.LoginForm
                             }
                             )
            else:
                return render(request,
                             'first_app/login.html',
                             {
                             'msg': 'Form Valid',
                             'form': forms.LoginForm
                             }
                             )
        else:
            return render(request,
                        'first_app/login.html',
                        {
                        'msg': 'Form Not Valid',
                        'form': forms.LoginForm
                        }
                        )
    else:
        return render(request,
                    'first_app/login.html',
                    {
                    'msg': 'Method is not POST',
                    'form': forms.LoginForm
                    }
                    )
