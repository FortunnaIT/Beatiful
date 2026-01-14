import random

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import title

from .forms import UserRegisterForm, ProfileForm
from .models import Profile
def register(request):
    title= 'Sign Up'
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profil.Objects.create(user=user)
            login(request,user)
            return redirect('login')
        else:
            return HttpResponse("Ma'lumotlar noto‘g‘ri")
    else:
        form = UserRegisterForm()

    return render(request, 'user/register.html', {'form': form})

def profile(request):
    title = 'Profile'
    user = request.user
    try:
       profile = Profile.objects.get(user=user)
    except:
        profile = Profile.objects.create(user=user)
    malumot={
        'user':user,
        'profile':profile
    }
    return render(request, 'user/profile.html', malumot)

def profile_edit(request):
    title = 'Edit Profile'
    Javob=""
    profile = Profile.objects.get(user=request.user)
    data = request.POST
    form = ProfileForm(instance=profile)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile.ism = data['ism']
            profile.family = data['familya']
            profile.tug_sana = data['tug_sana']
            profile.foto = request.FILES['foto']
            profile.nomer = data['nomer']
            profile.bio = data['bio']
            profile.save()
            profile = form.save(commit=False)

            return redirect('profile')
        else:
            Javob ="Oxshamadi"

    return render(request, 'user/profile_edit.html', {'form': form , 'Javob': Javob})


def passwort_reset_view(request):
    title = 'Password Reset'
    javob=""
    if request.method == "POST":
        deta = request.POST
        username = data = ['username']
        try:
            user = User.objects.get(username=username)
            email = user.email
            code = random.randint(100000, 1000000)
            print(code)
            request.session['code'] = code
            return redirect('verify_view')
        except:
            javob = "Oxshamadi"
    return render(request, 'user/password_reset.html', {'title':title , 'javob': javob})


def verify_view(request):
    title = 'Verify'
    javob=""
    if request.method == "POST":
        deta = request.POST
        code = deta['code']
        our_code = request.session.get('code')
        if code != our_code:
            javob = "Oxshamadi"
        else:
            return redirect('password_change')
    return render(request, 'user/verify_view.html', {'title': title, 'javob': javob})