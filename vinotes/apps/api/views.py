from django.contrib.auth.models import User
from rest_framework import generics
from .models import Note, Trait, Wine, Winery
from .serializers import NoteSerializer, TraitSerializer, WineSerializer, WinerySerializer, UserSerializer


class NoteList(generics.ListCreateAPIView):
    """
    List all tasting notes, or create a new tasting note.
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a tasting note.
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class TraitList(generics.ListCreateAPIView):
    """
    List all wine traits, or create a new wine trait.
    """
    queryset = Trait.objects.all()
    serializer_class = TraitSerializer


class TraitDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a wine trait.
    """
    queryset = Trait.objects.all()
    serializer_class = TraitSerializer


class WineList(generics.ListCreateAPIView):
    """
    List all wines, or create a new wine.
    """
    queryset = Wine.objects.all()
    serializer_class = WineSerializer


class WineDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a wine.
    """
    queryset = Wine.objects.all()
    serializer_class = WineSerializer


class WineryList(generics.ListCreateAPIView):
    """
    List all wineries, or create a new winery.
    """
    queryset = Winery.objects.all()
    serializer_class = WinerySerializer


class WineryDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a winery.
    """
    queryset = Winery.objects.all()
    serializer_class = WinerySerializer


class UserList(generics.ListAPIView):
    """
    List all users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    """
    Retrieve a user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer