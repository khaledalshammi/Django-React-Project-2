from rest_framework.decorators import api_view
from .serializers import NoteSerializers
from .models import Note
from rest_framework.response import Response

@api_view(['GET'])
def list(request):
    data = Note.objects.all().order_by('-updated')
    serializer = NoteSerializers(data,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def note_detail(request,pk):
    data = Note.objects.get(pk=pk)
    serializer = NoteSerializers(data)
    return Response(serializer.data)

@api_view(['POST'])
def add(request):
    data = request.data
    note = Note.objects.create(body=data['body'])
    serializer = NoteSerializers(note)
    return Response(serializer.data)

# @api_view(['POST'])
# def add(request):
#     serializer = NoteSerializers(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

@api_view(['PUT'])
def update(request,pk):
    data = Note.objects.get(pk=pk)
    serializer = NoteSerializers(instance=data,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete(request,pk):
    data = Note.objects.get(pk=pk)
    data.delete()
    return Response('Done')