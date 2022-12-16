from django.urls import path
from django.views.generic import TemplateView

from . import views
urlpatterns = [
    path('', views.home_view, name='home'),
    path('profile/', views.profile, name='profile'),
    path('files/<int:num>', views.files_view, name='files'),
    path('test/', TemplateView.as_view(template_name='Home/test.html')),
    path('post_detail/<int:num>/', views.detail_view, name='detail')
]
