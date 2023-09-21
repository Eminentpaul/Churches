from django.shortcuts import render, redirect
from .models import Artist, Album, Song, Sermon, Testimony, MusicFavorite, User
from django.contrib.auth.models import auth
from django.contrib import messages as mg
from django.contrib.auth.decorators import login_required
from .forms import AccountCreation


# Create your views here.
def home(request):
    songs = Song.objects.all()
    albums = Album.objects.all()
    sermons = Sermon.objects.all()
    testimonies = Testimony.objects.all()

    context = {
        "songs": songs,
        "albums": albums,
        "sermons": sermons,
        "testimonies": testimonies,
    }
    return render(request, "index.html", context)


def allArtist(request):
    artists = Artist.objects.all()

    context = {"artists": artists}
    return render(request, "about.html", context)


def login(request):
    login = True

    if request.method == "POST":
        email = request.POST.get("username")
        password = request.POST.get("password")

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("home")
        else:
            mg.error(request, "Invalid Username or Password")

    context = {"login": login}
    return render(request, "login.html", context)


def register(request):
    form = AccountCreation()

    if request.method == "POST":
        form = AccountCreation(request.POST)

        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect("home")
        else:
            mg.error(request, "Email Used already or Password nto strong ")

    context = {"form": form}
    return render(request, "login.html", context)


def album(request, pk):
    album = Album.objects.get(id=pk)
    songs = album.song_set.all()

    context = {"album": album, "songs": songs}

    return render(request, "album.html", context)


def artist(request, pk):
    artist = Artist.objects.get(id=pk)
    albums = artist.album_set.all()
    songs = Song.objects.all()

    context = {"artist": artist, "albums": albums, "songs": songs}

    return render(request, "artist.html", context)


def sermonDetails(request, pk):
    sermon = Sermon.objects.get(id=pk)

    context = {"sermon": sermon}
    return render(request, "sermon-details.html", context)


@login_required(login_url="login")
def favourites(request, pk):
    obj = Song.objects.get(id=pk)

    isAvailable = MusicFavorite.objects.filter(user=request.user, music=obj)

    if isAvailable:
        return redirect("home")
    else:
        MusicFavorite.objects.create(user=request.user, music=obj).save()
        return redirect("fav")


@login_required(login_url="login")
def favMusic(request):
    songs = MusicFavorite.objects.all()
    return render(request, "fav.html", {'songs': songs})


def logout(request):
    auth.logout(request)
    return redirect("home")
