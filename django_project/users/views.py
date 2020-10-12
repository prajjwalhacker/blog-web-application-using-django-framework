from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import profile_form,user_form
# Create your views here.



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            form.save()
            return redirect('login')

    else:
        form = UserCreationForm()
    
    return render(request,'users/register.html' , {'form' : form})

@login_required
def profile(request):
    u_form = user_form()
    p_form = profile_form()

    context = {
        'u_form' : u_form,
        'p_form': p_form
    }
    return render(request , 'users/profile.html', context)
