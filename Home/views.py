from django.shortcuts import render

# Create your views here.

# Home
from Home.models import PostModel


def home_view(request):
    return render(request, 'Home/home.html', {'user': request.user})


def profile(request):
    user = request.user
    contents = PostModel.objects.filter(user=user)
    context = {'user': user, 'con':contents}
    return render(request, 'Home/profile.html', context)


