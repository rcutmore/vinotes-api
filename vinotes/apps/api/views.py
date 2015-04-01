from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Note, Trait, Wine, Winery
from .serializers import NoteSerializer, TraitSerializer, WineSerializer, WinerySerializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def note_list(request):
    """
    List all tasting notes, or create a new tasting note.
    """
    if request.method == 'GET':
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = NoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONReponse(serializer.errors, status=400)


@csrf_exempt
def note_detail(request, pk):
    """
    Retrieve, update, or delete a tasting note.
    """
    try:
        note = Note.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = NoteSerializer(note)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = NoteSerializer(note, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        note.delete()
        return HttpResponse(status=204)


@csrf_exempt
def wine_list(request):
    """
    List all wines, or create a new wine.
    """
    if request.method == 'GET':
        wines = Wine.objects.all()
        serializer = WineSerializer(wines, many=True)
        return JSONResponse(serializer.data)

    elif requesst.method == 'POST':
        data = JSONParser().parse(request)
        serializer = WineSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def wine_detail(request, pk):
    """
    Retrieve, update, or delete a wine.
    """
    try:
        wine = Wine.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = WineSerializer(wine)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = WineSerializer(wine, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        wine.delete()
        return HttpResponse(status=204)


@csrf_exempt
def winery_list(request):
    """
    List all wineries, or create a new winery.
    """
    if request.method == 'GET':
        wineries = Winery.objects.all()
        serializer = WinerySerializer(wineries, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = WinerySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def winery_detail(request, pk):
    """
    Retrieve, update, or delete a winery.
    """
    try:
        winery = Winery.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = WinerySerializer(winery)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = WinerySerializer(winery, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)