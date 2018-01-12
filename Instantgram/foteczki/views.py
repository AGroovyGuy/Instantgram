from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse
from django.views import View
from .models import Photo
from django.db.models import Avg
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import UserPassesTestMixin
import hashlib


class HubView(View):
    def get(self, request):
        ctx = {"posts": Photo.objects.all().order_by("-creation_date")}
        return render(request, "hub.html", ctx)

