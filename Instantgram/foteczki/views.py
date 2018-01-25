from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse
from django.views import View
from .models import Photo, Likes
from .forms import PhotoUploadForm
from Instantgram.settings import MEDIA_ROOT, MEDIA_URL
from django.db.models import Avg
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import UserPassesTestMixin
import hashlib
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm, PhotoUploadForm


class HubView(View):
    def get(self, request):
        form = PhotoUploadForm
        success_url = '/static/'
        ctx = {"posts": Photo.objects.all().order_by("-creation_date"), "form":form}
        return render(request, "hub.html")

    def post(self, request):
        form = PhotoUploadForm(request.POST)
        ctx = {"posts": Photo.objects.all().order_by("-creation_date"), "form":form}
        if form.is_valid():
            contents = Photo.objects.create(description=form.cleaned_data["description"],
                                            op=self.request.user,
                                                photo=form.cleaned_data["photo"])
        return render(request, "hub.html", ctx)


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "hub.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data["nickname"]
            password = form.cleaned_data["password"]
            auth = authenticate(username=nickname, password=password)
            if auth:
                login(request, auth)
                return HttpResponseRedirect('/hub')
            else:
                return HttpResponse("Błędny login lub hasło.")
        return render(request, "hub.html", {"form": form})