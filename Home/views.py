from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from Accounts.forms import SearchForm
from Accounts.models import Profile
from Home.forms import fileForm
from Home.models import PostModel
from django.contrib import messages


def home_view(request):
    form = SearchForm(request.GET)
    names = Profile.objects.all()
    if form.is_valid():
        if request.user.is_authenticated:
            names = Profile.objects.filter(user__username__contains=form.cleaned_data['name']).exclude(
                user=request.user)
        else:
            names = Profile.objects.filter(user__username__contains=form.cleaned_data['name'])
    context = {'user': request.user,
               'names': names,
               'form': form}
    return render(request, 'Home/home.html', context)


@login_required
def profile(request):
    user = request.user

    if request.method == 'POST':
        form = fileForm(request.POST, files=request.FILES)
        if form.is_valid():
            # form.save()
            title = form.cleaned_data['title']
            content = request.FILES['content']
            desc = form.cleaned_data['desc']

            if Profile.objects.get(user=user).computing_size(content.size):

                PostModel.objects.create(title=title, content=content, desc=desc, user=request.user)
                messages.success(request, 'upload successfully')
            else:
                messages.error(request, 'you are not have enough size')
    else:
        form = fileForm()
    contents = PostModel.objects.filter(user=user)
    context = {'user': user,
               'con': contents,
               'form': form}
    return render(request, 'Home/profile.html', context)


def files_view(request, num):
    pro = Profile.objects.get(user_id=num)
    posts = PostModel.objects.filter(user_id=num)
    context = {'posts': posts,
               'pro': pro}
    return render(request, 'Home/files.html', context)


@login_required
def detail_view(request, num):
    post = PostModel.objects.get(pk=num)
    return render(request, 'Home/post.html', {'post': post})
