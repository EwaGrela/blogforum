from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import User
# Create your views here.
class UserList(ListView):
    model = User
    template_name = "user_list"


class UserDetail(DetailView):
    model = User
    # template_name = "user_detail"