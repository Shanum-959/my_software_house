from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm  # You will need to create this form

# User signup
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create a blank profile for the new user
            UserProfile.objects.create(user=user)
            return redirect('accounts:login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


# View profile
@login_required
def profile_view(request):
    profile = UserProfile.objects.get(user=request.user)
    return render(request, 'accounts/profile.html', {'profile': profile})


# Edit profile
@login_required
def edit_profile_view(request):
    profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'accounts/edit_profile.html', {'form': form})


# Optional: Home view for accounts
@login_required
def accounts(request):
    return render(request, 'accounts/accounts.html')
