from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .forms import CategorySelectionForm

@login_required
def home(request):
    return render(request, 'home.html')

def user_registration_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('category_selection')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def user_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def category_selection_view(request):
    if request.method == 'POST':
        form = CategorySelectionForm(request.POST)
        if form.is_valid():
            selected_categories = form.cleaned_data['categories']
            # Process selected categories (e.g., save to user profile)
            return redirect('home')
    else:
        form = CategorySelectionForm()
    return render(request, 'category_selection.html', {'form': form})
