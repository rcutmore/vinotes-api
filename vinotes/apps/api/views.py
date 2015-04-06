from django.contrib.auth.models import User
from rest_framework import generics, permissions
from .models import Note, Trait, Wine, Winery
from .serializers import NoteSerializer, TraitSerializer, WineSerializer, WinerySerializer, UserSerializer


class NoteList(generics.ListCreateAPIView):
    """
    List all tasting notes, or create a new tasting note.
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (permissions.IsAuthenticated,)


    def perform_create(self, serializer):
        serializer.save(taster=self.request.user)


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a tasting note.
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (permissions.IsAuthenticated,)


class TraitList(generics.ListCreateAPIView):
    """
    List all wine traits, or create a new wine trait.
    """
    queryset = Trait.objects.all()
    serializer_class = TraitSerializer
    permission_classes = (permissions.IsAuthenticated,)


class TraitDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a wine trait.
    """
    queryset = Trait.objects.all()
    serializer_class = TraitSerializer
    permission_classes = (permissions.IsAuthenticated,)


class WineList(generics.ListCreateAPIView):
    """
    List all wines, or create a new wine.
    """
    queryset = Wine.objects.all()
    serializer_class = WineSerializer
    permission_classes = (permissions.IsAuthenticated,)


class WineDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a wine.
    """
    queryset = Wine.objects.all()
    serializer_class = WineSerializer
    permission_classes = (permissions.IsAuthenticated,)


class WineryList(generics.ListCreateAPIView):
    """
    List all wineries, or create a new winery.
    """
    queryset = Winery.objects.all()
    serializer_class = WinerySerializer
    permission_classes = (permissions.IsAuthenticated,)


class WineryDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a winery.
    """
    queryset = Winery.objects.all()
    serializer_class = WinerySerializer
    permission_classes = (permissions.IsAuthenticated,)


class UserList(generics.ListAPIView):
    """
    List all users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)


class UserDetail(generics.RetrieveAPIView):
    """
    Retrieve a user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)