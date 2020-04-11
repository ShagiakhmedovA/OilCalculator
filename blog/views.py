from django.utils import timezone
from .models import Post, Calculation
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .forms import PostForm, UserForm, CalculationForm
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'pages/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'pages/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'pages/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.edit_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'pages/post_edit.html', {'form': form})


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return HttpResponseRedirect('/')


def get_user_profile(request, pk):
    user = User.objects.get(pk=pk)
    return render(request, 'registration/user_profile.html', {'user':user})


def edit_user_profile(request, pk):
    user = get_object_or_404(User,pk=request.user.pk)
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES or None, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('user_profile', pk=user.pk)
    else:
        form = UserForm(instance=user)
    return render(request, 'registration/user_profile_edit.html', {'form': form})


def theory(request):
    return render(request, 'pages/theory.html')


def about_program(request):
    return render(request, 'pages/about_program.html')


def calculation_new(request):
    if request.method == "POST":
        form = CalculationForm(request.POST)
        if form.is_valid():
            calculation = form.save(commit=False)
            calculation.author = request.user
            
            calculation.date = timezone.now()
            calculation.save()
            return redirect('calculation_detail', pk=calculation.pk)
    else:
        form = CalculationForm()
    return render(request, 'pages/calculation_new.html', {'form': form})


def history_show(request):
    calculations = Calculation.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'pages/history.html', {'calculations': calculations})


def calculation_detail(request, pk):
    calculation = get_object_or_404(Calculation, pk=pk)
    return render(request, 'pages/Calculation_detail.html', {'calculation': calculation},)


def calculation_delete(request, pk):
    try:
        calculation = get_object_or_404(Calculation, pk=pk)
        calculation.delete()
        calculations = Calculation.objects.filter(date__lte=timezone.now()).order_by('date')
        return render(request, 'pages/history.html', {'calculations': calculations})

    except ValueError:
        return render(request, 'pages/history.html')
