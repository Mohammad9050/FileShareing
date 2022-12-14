from django.shortcuts import render

# Create your views here.

# Home
from Accounts.models import Profile
from Home.forms import fileForm
from Home.models import PostModel


def home_view(request):
    return render(request, 'Home/home.html', {'user': request.user})


def profile(request):
    user = request.user

    if request.method == 'POST':
        form = fileForm(request.POST, files=request.FILES)
        if form.is_valid():
            # form.save()
            title = form.cleaned_data['title']
            content = request.FILES['content']
            desc = form.cleaned_data['desc']

            print('hi')
            if Profile.objects.get(user=user).computing_size(content.size):
                print(content.size)

                PostModel.objects.create(title=title, content=content, desc=desc, user=request.user)
            else:
                print('size is full')
    else:
        form = fileForm()
    contents = PostModel.objects.filter(user=user)
    context = {'user': user,
               'con': contents,
               'form': form}
    return render(request, 'Home/profile.html', context)
