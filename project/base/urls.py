from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('all/artists', views.allArtist, name='all-artist'),
    path('albums/<str:pk>/details', views.album, name='album'),
    path('favourite/<str:pk>/', views.favourites, name='favourite'),
    path('artist/<str:pk>/details', views.artist, name='artist'),
    path('sermon/<str:pk>/details', views.sermonDetails, name='sermon'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('My/favorites/music', views.favMusic, name='fav'),
    path('logout/', views.logout, name='logout')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)