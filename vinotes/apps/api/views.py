from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Note, Trait, Wine, Winery
from .serializers import NoteSerializer, TraitSerializer, WineSerializer, WinerySerializer


@api_view(['GET', 'POST'])
def note_list(request, format=None):
    """
    List all tasting notes, or create a new tasting note.
    """
    if request.method == 'GET':
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Reponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def note_detail(request, pk, format=None):
    """
    Retrieve, update, or delete a tasting note.
    """
    try:
        note = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NoteSerializer(note)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = NoteSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def trait_list(request, format=None):
    """
    List all wine traits, or create a new wine trait.
    """
    if request.method == 'GET':
        traits = Trait.objects.all()
        serializer = TraitSerializer(traits, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TraitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def trait_detail(request, pk, format=None):
    """
    Retrieve, update, or delete a wine trait.
    """
    try:
        trait = Trait.objects.get(pk=pk)
    except Trait.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TraitSerializer(trait)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TraitSerializer(trait, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        trait.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def wine_list(request, format=None):
    """
    List all wines, or create a new wine.
    """
    if request.method == 'GET':
        wines = Wine.objects.all()
        serializer = WineSerializer(wines, many=True)
        return Response(serializer.data)

    elif requesst.method == 'POST':
        serializer = WineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def wine_detail(request, pk, format=None):
    """
    Retrieve, update, or delete a wine.
    """
    try:
        wine = Wine.objects.get(pk=pk)
    except Wine.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WineSerializer(wine)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = WineSerializer(wine, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        wine.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def winery_list(request, format=None):
    """
    List all wineries, or create a new winery.
    """
    if request.method == 'GET':
        wineries = Winery.objects.all()
        serializer = WinerySerializer(wineries, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = WinerySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def winery_detail(request, pk, format=None):
    """
    Retrieve, update, or delete a winery.
    """
    try:
        winery = Winery.objects.get(pk=pk)
    except Winery.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WinerySerializer(winery)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = WinerySerializer(winery, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        winery.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)