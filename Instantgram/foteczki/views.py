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
from .forms import LoginForm, PhotoUploadForm, CreateAccountForm


@method_decorator(login_required, name='dispatch')
class HubView(View):
    def get(self, request):
        posts = Photo.objects.all().order_by("-creation_date")
        likes_dict = {}
        for photo in posts:
            likes_dict.update({photo.id: Likes.objects.filter(photo_id=photo.id).count()})
        return render(request, 'hub.html', {'posts': posts, 'likes_dict': likes_dict})

    def post(self, request):
        posts = Photo.objects.all().order_by("-creation_date")
        photo_id = request.POST.get('photo_id')
        photo = Photo.objects.get(pk=photo_id)
        likes = Likes.objects.filter(user_id=request.user).filter(photo_id=photo_id).count()
        if likes == 0:
            new_like = Likes.objects.create(photo_id=photo,
                                            user_id=request.user)
        else:
            Likes.objects.filter(photo_id=photo_id, user_id=request.user).delete()
        return HttpResponseRedirect('/hub')



@method_decorator(login_required, name='dispatch')
class AddPhotoView(View):
    def get(self, request):
        form = PhotoUploadForm()
        ctx = {"form": form}
        return render(request, "addphoto.html", ctx)
    def post(self, request):
        form = PhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            contents = Photo.objects.create(description=form.cleaned_data["description"],
                                            op=self.request.user,
                                                photo=form.cleaned_data["photo"])
        return HttpResponseRedirect('/hub')


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "form-show.html", {"form": form})

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
        return render(request, "form-show.html", {"form": form})



class CreateAccountView(View):
    def get(self, request):
        form = CreateAccountForm()
        return render(request, "form-show.html", {"form": form})

    def post(self, request):
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data["nickname"]).count() > 0:
                messages.info(request, 'Istnieje już użytkownik o takim nicku.')
                return HttpResponseRedirect('/createuser')
            elif User.objects.filter(email=form.cleaned_data["mail"]).count() > 0:
                messages.info(request, 'Konto o podanym mailu już istnieje.')
                return HttpResponseRedirect('/createuser')
            User.objects.create_user(username=form.cleaned_data["nickname"],
                                                 password=form.cleaned_data["password"],
                                                 email=form.cleaned_data["mail"])
            return HttpResponseRedirect('/')


@method_decorator(login_required, name='dispatch')
class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')