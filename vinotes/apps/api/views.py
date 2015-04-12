from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Note, Trait, Wine, Winery
from .serializers import NoteSerializer, TraitSerializer, WineSerializer, WinerySerializer, UserSerializer


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'notes': reverse('note-list', request=request, format=format),
        'traits': reverse('trait-list', request=request, format=format),
        'wines': reverse('wine-list', request=request, format=format),
        'wineries': reverse('winery-list', request=request, format=format),
    })


class NoteList(generics.ListCreateAPIView):
    """
    List all tasting notes, or create a new tasting note.
    """
    serializer_class = NoteSerializer
    permission_classes = (permissions.IsAuthenticated,)


    def get_queryset(self):
        return Note.objects.filter(taster=self.request.user)


    def perform_create(self, serializer):
        serializer.save(taster=self.request.user)


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a tasting note.
    """
    serializer_class = NoteSerializer
    permission_classes = (permissions.IsAuthenticated,)


    def get_queryset(self):
        return Note.objects.filter(taster=self.request.user)


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
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)


    def get_queryset(self):
        return User.objects.filter(email=self.request.user.email)


class UserDetail(generics.RetrieveAPIView):
    """
    Retrieve a user.
    """
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)


    def get_queryset(self):
        return User.objects.filter(email=self.request.user.email)