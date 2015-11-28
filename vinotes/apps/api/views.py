"""
Contains views for API app.
"""
from django.contrib.auth import get_user_model

from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Note, Trait, Wine, Winery
from .permissions import IsAuthenticatedOrRegistering
from .serializers import (
    NoteSerializer,
    TraitSerializer,
    WineSerializer,
    WinerySerializer,
    UserSerializer,
)


@api_view(('GET',))
def api_root(request, format=None):
    """Render response for API root.

    :param request: :class:`Request` object.
    :param format: Requested format type (HTML, JSON).
    :returns: :class:`Response` object.
    """
    return Response({
        'notes': reverse('note-list', request=request, format=format),
        'traits': reverse('trait-list', request=request, format=format),
        'wines': reverse('wine-list', request=request, format=format),
        'wineries': reverse('winery-list', request=request, format=format),
    })


class NoteList(generics.ListCreateAPIView):
    """List all tasting notes or create a new tasting note."""
    serializer_class = NoteSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        """Fetch all notes for request's user."""
        return Note.objects.filter(taster=self.request.user)

    def perform_create(self, serializer):
        """Set request's user as taster of note."""
        serializer.save(taster=self.request.user)


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update, or delete a tasting note."""
    serializer_class = NoteSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        """Fetch all notes for request's user."""
        return Note.objects.filter(taster=self.request.user)


class TraitList(generics.ListCreateAPIView):
    """List all wine traits or create a new wine trait."""
    queryset = Trait.objects.all()
    serializer_class = TraitSerializer
    permission_classes = (permissions.IsAuthenticated,)


class TraitDetail(generics.RetrieveAPIView):
    """Retrieve a wine trait."""
    queryset = Trait.objects.all()
    serializer_class = TraitSerializer
    permission_classes = (permissions.IsAuthenticated,)


class WineList(generics.ListCreateAPIView):
    """List all wines or create a new wine."""
    queryset = Wine.objects.all()
    serializer_class = WineSerializer
    permission_classes = (permissions.IsAuthenticated,)


class WineDetail(generics.RetrieveAPIView):
    """Retrieve a wine."""
    queryset = Wine.objects.all()
    serializer_class = WineSerializer
    permission_classes = (permissions.IsAuthenticated,)


class WineryList(generics.ListCreateAPIView):
    """List all wineries or create a new winery."""
    queryset = Winery.objects.all()
    serializer_class = WinerySerializer
    permission_classes = (permissions.IsAuthenticated,)


class WineryDetail(generics.RetrieveAPIView):
    """Retrieve a winery."""
    queryset = Winery.objects.all()
    serializer_class = WinerySerializer
    permission_classes = (permissions.IsAuthenticated,)


class UserList(generics.ListCreateAPIView):
    """List all users."""
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrRegistering,)

    def get_queryset(self):
        """Fetch users with the email matching request's user."""
        return get_user_model().objects.filter(email=self.request.user.email)


class UserDetail(generics.RetrieveAPIView):
    """Retrieve a user."""
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        """Fetch users with email matching request's user."""
        return get_user_model().objects.filter(email=self.request.user.email)
