from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.http import require_http_methods

@require_http_methods(['GET', 'POST'])
def sign_up(request):
    if request.user.is_authenticated:
        return redirect('pages:home')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = UserCreationForm()

    context = {
        'form': form
    }
    
    return render(request, 'registration/sign_up.html', context)