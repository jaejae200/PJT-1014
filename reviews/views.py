from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm

# Create your views here.

@login_required
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews:index')
    else: 
        form = ReviewForm()
    context = {
        'form': form
    }
    return render(request, 'reviews/form.html', context=context)