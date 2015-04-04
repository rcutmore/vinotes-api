from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Note, Trait, Wine, Winery
from .serializers import NoteSerializer, TraitSerializer, WineSerializer, WinerySerializer


class NoteList(APIView):
    """
    List all tasting notes, or create a new tasting note.
    """
    def get(self, request, format=None):
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NoteDetail(APIView):
    """
    Retrieve, update, or delete a tasting note.
    """
    def get_object(self, pk):
        try:
            return Note.objects.get(pk=pk)
        except Note.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        note = self.get_object(pk)
        serializer = NoteSerializer(note)
        return Response(serializer.data)


    def put(self, request, pk, format=None):
        note = self.get_object(pk)
        serializer = NoteSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        note = self.get_object(pk)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TraitList(APIView):
    """
    List all wine traits, or create a new wine trait.
    """
    def get(self, request, format=None):
        traits = Trait.objects.all()
        serializer = TraitSerializer(traits, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = TraitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TraitDetail(APIView):
    """
    Retrieve, update, or delete a wine trait.
    """
    def get_object(self, pk):
        try:
            return Trait.objects.get(pk=pk)
        except Trait.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        trait = self.get_object(pk)
        serializer = TraitSerializer(trait)
        return Response(serializer.data)


    def put(self, request, pk, format=None):
        trait = self.get_object(pk)
        serializer = TraitSerializer(trait, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        trait = self.get_object(pk)
        trait.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WineList(APIView):
    """
    List all wines, or create a new wine.
    """
    def get(self, request, format=None):
        wines = Wine.objects.all()
        serializer = WineSerializer(wines, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = WineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WineDetail(APIView):
    """
    Retrieve, update, or delete a wine.
    """
    def get_object(self, pk):
        try:
            return Wine.objects.get(pk=pk)
        except Wine.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        wine = self.get_object(pk)
        serializer = WineSerializer(wine)
        return Response(serializer.data)


    def put(self, request, pk, format=None):
        wine = self.get_object(pk)
        serializer = WinerySerializer(wine, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        wine = self.get_object(pk)
        wine.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WineryList(APIView):
    """
    List all wineries, or create a new winery.
    """
    def get(self, request, format=None):
        wineries = Winery.objects.all()
        serializer = WinerySerializer(wineries, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = WinerySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WineryDetail(APIView):
    """
    Retrieve, update, or delete a winery.
    """
    def get_object(self, pk):
        try:
            return Winery.objects.get(pk=pk)
        except Winery.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        winery = self.get_object(pk)
        serializer = WinerySerializer(winery)
        return Response(serializer.data)


    def put(self, request, pk, format=None):
        winery = self.get_object(pk)
        serializer = WinerySerializer(winery, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        winery = self.get_object(pk)
        winery.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)